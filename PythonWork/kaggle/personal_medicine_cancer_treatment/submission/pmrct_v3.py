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

    print yet_to_complete.isnull().sum()
    print '**********************'
   
    encoder = LabelEncoder()
    y_train = train['Class'].values
    encoder.fit(y_train)
    encoded_y = encoder.transform(y_train)


    rf = RandomForestClassifier(n_estimators=100,min_samples_split=5)
    rf.fit(yet_to_complete[:3321],encoded_y)
    y_pred=rf.predict(yet_to_complete[3321:])

    print '*************************************'

    print type(y_pred), len(y_pred)

    print y_pred[0]
    print y_pred[1]
    print y_pred[2]
    print y_pred[3]
    print y_pred[4]

    print '***************************************'


    # #gbm algorithm with random parameters
    # gbm1=GradientBoostingClassifier(learning_rate=0.1, min_samples_split=500,min_samples_leaf=50,max_depth=8,max_features='sqrt',subsample=0.8,random_state=10)
    # gbm1.fit(yet_to_complete[:3321],encoded_y)

    # #predictions
    # y_pred=gbm1.predict_proba(yet_to_complete[3321:])



    testing_merge_df=testing_merge_df.drop('Gene', axis=1)
    testing_merge_df=testing_merge_df.drop('Variation', axis=1)
    testing_merge_df=testing_merge_df.drop('Text', axis=1)
    
    testing_merge_df['predicted_class'] = y_pred

    onehot = pd.get_dummies(testing_merge_df['predicted_class'])
    testing_merge_df = testing_merge_df.join(onehot)
    testing_merge_df=testing_merge_df.drop('predicted_class', axis=1)
    print testing_merge_df.head(8) 

    submission_df = testing_merge_df[['ID',1,2,3,4,5,6,8]]
    submission_df.columns = [['ID','class1','class2','class3','class4','class5','class6','class8']]
    print submission_df.head(10)

    submission_df['class9']=0
    submission_df.insert(7,'class7',0)
    print '******************************8'
    print submission_df.head(10)
  

    submission_df.to_csv('submission_rf.csv', index=False)

    # X_test_final = testing_merge_df['Text'].values

    # # predicted_class = text_clf.predict(X_test_final)
    # testing_merge_df['predicted_class'] = y_pred

    # print testing_merge_df.head(8) 

    # onehot = pd.get_dummies(testing_merge_df['predicted_class'])
    # testing_merge_df = testing_merge_df.join(onehot)

    # submission_df = testing_merge_df[["ID",1,2,3,4,5,6,7,8,9]]
    # submission_df.columns = ['ID', 'class1','class2','class3','class4','class5','class6','class7','class8','class9']
    # submission_df.head(5)

    # submission_df.to_csv('submission.csv', index=False)




    #tweaking the submission file as required
    # onehot = pd.get_dummies(y_pred)
    # print onehot[0]
    # subm_file = pd.DataFrame(onehot)
    # print subm_file.columns
    # # subm_file= subm_file.drop('predicted_class', axis=1)
    # subm_file['id'] = test_index
    # subm_file.columns = ['class1', 'class2', 'class3', 'class4', 'class5', 'class6', 'class7', 'class8', 'class9']
    # subm_file=subm_file.reset_index()
    # # subm_file.columns[0]=['ID']
    # subm_file=subm_file.index

    # subm_file.to_csv("submission_rf.csv",index=False)



   

if __name__=='__main__':
    main()