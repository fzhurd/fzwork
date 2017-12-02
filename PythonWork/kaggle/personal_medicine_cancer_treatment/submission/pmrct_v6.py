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

from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import BernoulliRBM


def main():

    train_variant = pd.read_csv("../input/training_variants")
    test_variant = pd.read_csv("../input/test_variants")
    train_text = pd.read_csv("../input/training_text", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])
    test_text = pd.read_csv("../input/test_text", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])
    train = pd.merge(train_variant, train_text, how='left', on='ID')
    x_train = train.drop('Class', axis=1)

    testing_variants_df = pd.read_csv("../input/test_variants")
    testing_text_df = pd.read_csv("../input/test_text", sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])
    testing_merge_df = testing_variants_df.merge(testing_text_df,left_on="ID",right_on="ID")


    x_test = pd.merge(test_variant, test_text, how='left', on='ID')
    test_index = x_test['ID'].values
    # number of test data : 5668

    data = np.concatenate((x_train, x_test), axis=0)
    data=pd.DataFrame(data)
    data.columns = ["ID", "Gene", "Variation", "Text"]

    #TFIDF
    mod=TfidfVectorizer(min_df=5, max_features=500, stop_words='english')
    mod_TD=mod.fit_transform(data.Text)

    #SVD features
    SVD=TruncatedSVD(200,random_state=41)
    SVD_FIT=SVD.fit_transform(mod_TD)
    yet_to_complete=pd.DataFrame(SVD_FIT)

    encoder = LabelEncoder()
    y_train = train['Class'].values
    encoder.fit(y_train)
    encoded_y = encoder.transform(y_train)

    # nnc=BernoulliRBM(random_state=0, verbose=True)
    # nnc.fit(yet_to_complete[:3321],encoded_y)
    # y_pred=nnc.predict(yet_to_complete[3321:])

    from sklearn.neighbors import KNeighborsClassifier 

    knnClf=KNeighborsClassifier(n_neighbors=5)
    knnClf.fit(yet_to_complete[:3321],encoded_y)  
    y_pred=knnClf.predict(yet_to_complete[3321:])  

    x_test['predicted_class'] = y_pred

    onehot = pd.get_dummies(x_test['predicted_class'])
    testing_merge_df = x_test.join(onehot)

    print testing_merge_df.head(10)



    submission_df = testing_merge_df[["ID",1,2,3,4,5,6,7,8]]
    submission_df.columns = ['ID', 'class1','class2','class3','class4','class5','class6','class7','class8']

    testing_merge_df=testing_merge_df.drop('Gene', axis=1)
    testing_merge_df=testing_merge_df.drop('Variation', axis=1)
    testing_merge_df=testing_merge_df.drop('Text', axis=1)
    
    # testing_merge_df['predicted_class'] = y_pred

    # onehot = pd.get_dummies(testing_merge_df['predicted_class'])
    # testing_merge_df = testing_merge_df.join(onehot)
    # testing_merge_df=testing_merge_df.drop('predicted_class', axis=1)
 
    # submission_df = testing_merge_df[['ID',1,2,3,4,5,6,8]]
    # submission_df.columns = [['ID','class1','class2','class3','class4','class5','class6','class8']]

    submission_df['class9']=0
    # submission_df.insert(7,'class7',0)


    submission_df.to_csv('submission_knn.csv', index=False)




   

if __name__=='__main__':
    main()