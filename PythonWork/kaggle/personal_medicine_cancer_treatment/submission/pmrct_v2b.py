#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 

from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingClassifier


def main():
    train_variant = pd.read_csv("../input/training_variants")
    test_variant = pd.read_csv("../input/test_variants")
    test_stage2_variant = pd.read_csv("../input/stage2/stage2_test_variants.csv")

    train_text = pd.read_csv("../input/training_text", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])
    test_text = pd.read_csv("../input/test_text", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])
    test_stage2_text = pd.read_csv("../input/stage2/stage2_test_text.csv", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])

    train = pd.merge(train_variant, train_text, how='left', on='ID')
    x_train = train.drop('Class', axis=1)
    # number of train data : 3321

    x_test = pd.merge(test_variant, test_text, how='left', on='ID')
    test_index = x_test['ID'].values

    # number of test data : 5668
    x_test_stage2=pd.merge(test_stage2_variant, test_stage2_text, how='left', on='ID')
    test_index2= x_test_stage2['ID'].values
    data = np.concatenate((x_train, x_test), axis=0)
    data=pd.DataFrame(data)
    data2=pd.DataFrame(x_test_stage2)

    data.columns = ["ID", "Gene", "Variation", "Text"]
    data2.columns = ["ID", "Gene", "Variation", "Text"]

    #TFIDF
    mod=TfidfVectorizer(min_df=5, max_features=500, stop_words='english')
    mod_TD=mod.fit_transform(data.Text)

    mod_TD2=mod.fit_transform(data2.Text)


    #SVD features
    SVD=TruncatedSVD(200,random_state=41)
    SVD_FIT=SVD.fit_transform(mod_TD)
    SVD_FIT2= SVD.fit_transform(mod_TD2)

    yet_to_complete=pd.DataFrame(SVD_FIT)
    yet_to_complete2=pd.DataFrame(SVD_FIT2)
    #data.drop(data.columns[[0,3]],inplace=True, axis=1)
    #as Gene and Variation data values are just scattered like IDS, i dont think these give u great info about the prediction
    encoder = LabelEncoder()
    y_train = train['Class'].values
    encoder.fit(y_train)
    encoded_y = encoder.transform(y_train)

    #gbm algorithm with random parameters
    gbm1=GradientBoostingClassifier(learning_rate=0.1, min_samples_split=500,min_samples_leaf=50,max_depth=8,max_features='sqrt',subsample=0.8,random_state=10)
    gbm1.fit(yet_to_complete[:3321],encoded_y)

    #predictions
    # y_pred=gbm1.predict_proba(yet_to_complete[3321:])
    y_pred2=gbm1.predict_proba(yet_to_complete2[0:])

    #tweaking the submission file as required
    # subm_file = pd.DataFrame(y_pred)
    # subm_file['id'] = test_index
    # subm_file.columns = ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7', 'class8', 'class9', 'id']
    # subm_file.to_csv("submission.csv",index=False)
    subm_file = pd.DataFrame(y_pred2)
    print len(subm_file)
    print len(test_index2)
    subm_file['id'] = test_index2
    
    subm_file.columns = ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7', 'class8', 'class9', 'id']
    subm_file.to_csv("submission2.csv",index=False)



   

if __name__=='__main__':
    main()