#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn import tree
import time
from functools import wraps

from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.cross_validation import StratifiedKFold
from sklearn.grid_search import GridSearchCV
from sklearn.ensemble.gradient_boosting import GradientBoostingClassifier
from sklearn.cross_validation import cross_val_score

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.regularizers import l2, l1
from sklearn.preprocessing import StandardScaler


def monitor_time(func):

    @wraps(func)
    def calculate_time(*args, **kwargs ):
        start_time = time.time()
        result=func(*args, **kwargs)
        end_time=time.time()
        cost_time=end_time-start_time
        print(cost_time)
        return result

    return calculate_time


class Titanic_Data(object):

    pd.options.display.max_columns = 100
    pd.options.display.max_rows = 100

    def __init__(self, train_file, test_file, combined=None):

        self.train_file = train_file
        self.test_file=test_file

        if combined is None:
            combined=[]
        self.combined=combined

        self.preprocess(train_file)

    def preprocess(self, file):

        data = pd.read_csv(file)

        print (data.head(5))

        data['Age'].fillna(data['Age'].median(), inplace=True)

        survived_sex = data[data['Survived']==1]['Sex'].value_counts()
        dead_sex = data[data['Survived']==0]['Sex'].value_counts()
        df = pd.DataFrame([survived_sex,dead_sex])
        df.index = ['Survived','Dead']
        df.plot(kind='bar',stacked=True, figsize=(15,8))

        survived_embark = data[data['Survived']==1]['Embarked'].value_counts()
        dead_embark = data[data['Survived']==0]['Embarked'].value_counts()
        df = pd.DataFrame([survived_embark,dead_embark])
        df.index = ['Survived','Dead']
        df.plot(kind='bar',stacked=True, figsize=(15,8))


    def status(self, feature):

        print ('Processing',feature,': ok')


    def get_combined_data(self, train_file, test_file):

        train = pd.read_csv(train_file)
        test = pd.read_csv(test_file)

        # extracting and then removing the targets from the training data 
        targets = train.Survived
        train.drop('Survived',1,inplace=True)
        
        # merging train data and test data for future feature engineering
        self.combined = train.append(test)
        self.combined.reset_index(inplace=True)
        self.combined.drop('index',inplace=True,axis=1)
        
        return self.combined

    def get_titles(self, combined):
       
        # we extract the title from each name
        combined['Title'] = combined['Name'].map(lambda name:name.split(',')[1].split('.')[0].strip())
        
        # a map of more aggregated titles
        Title_Dictionary = {
                            "Capt":       "Officer",
                            "Col":        "Officer",
                            "Major":      "Officer",
                            "Jonkheer":   "Royalty",
                            "Don":        "Royalty",
                            "Sir" :       "Royalty",
                            "Dr":         "Officer",
                            "Rev":        "Officer",
                            "the Countess":"Royalty",
                            "Dona":       "Royalty",
                            "Mme":        "Mrs",
                            "Mlle":       "Miss",
                            "Ms":         "Mrs",
                            "Mr" :        "Mr",
                            "Mrs" :       "Mrs",
                            "Miss" :      "Miss",
                            "Master" :    "Master",
                            "Lady" :      "Royalty"

                            }
        
        # we map each title
        combined['Title'] = combined.Title.map(Title_Dictionary)
        return combined

    def process_age(self, combined):
        
        
        # a function that fills the missing values of the Age variable
        def fillAges(row):
            if row['Sex']=='female' and row['Pclass'] == 1:
                if row['Title'] == 'Miss':
                    return 30
                elif row['Title'] == 'Mrs':
                    return 45
                elif row['Title'] == 'Officer':
                    return 49
                elif row['Title'] == 'Royalty':
                    return 39

            elif row['Sex']=='female' and row['Pclass'] == 2:
                if row['Title'] == 'Miss':
                    return 20
                elif row['Title'] == 'Mrs':
                    return 30

            elif row['Sex']=='female' and row['Pclass'] == 3:
                if row['Title'] == 'Miss':
                    return 18
                elif row['Title'] == 'Mrs':
                    return 31

            elif row['Sex']=='male' and row['Pclass'] == 1:
                if row['Title'] == 'Master':
                    return 6
                elif row['Title'] == 'Mr':
                    return 41.5
                elif row['Title'] == 'Officer':
                    return 52
                elif row['Title'] == 'Royalty':
                    return 40

            elif row['Sex']=='male' and row['Pclass'] == 2:
                if row['Title'] == 'Master':
                    return 2
                elif row['Title'] == 'Mr':
                    return 30
                elif row['Title'] == 'Officer':
                    return 41.5

            elif row['Sex']=='male' and row['Pclass'] == 3:
                if row['Title'] == 'Master':
                    return 6
                elif row['Title'] == 'Mr':
                    return 26
        
        combined.Age = combined.apply(lambda r : fillAges(r) if np.isnan(r['Age']) else r['Age'], axis=1)
        
        self.status('age')
        return combined

    def process_names(self, combined):
        
        # we clean the Name variable
        combined.drop('Name',axis=1,inplace=True)
        
        # encoding in dummy variable
        titles_dummies = pd.get_dummies(combined['Title'],prefix='Title')
        combined = pd.concat([combined,titles_dummies],axis=1)
        
        # removing the title variable
        combined.drop('Title',axis=1,inplace=True)
        
        self.status('names')

        return combined

    def process_fares(self, combined):
        
        # there's one missing fare value - replacing it with the mean.
        combined.Fare.fillna(combined.Fare.mean(),inplace=True)
        
        self.status('fare')
        return combined

    def process_embarked(self, combined):
        
        # two missing embarked values - filling them with the most frequent one (S)
        combined.Embarked.fillna('S',inplace=True)
        
        # dummy encoding 
        embarked_dummies = pd.get_dummies(combined['Embarked'],prefix='Embarked')
        combined = pd.concat([combined,embarked_dummies],axis=1)
        combined.drop('Embarked',axis=1,inplace=True)
        
        self.status('embarked')
        return combined

    def process_cabin(self, combined):
          
        # replacing missing cabins with U (for Uknown)
        combined.Cabin.fillna('U',inplace=True)
        
        # mapping each Cabin value with the cabin letter
        combined['Cabin'] = combined['Cabin'].map(lambda c : c[0])
        
        # dummy encoding ...
        cabin_dummies = pd.get_dummies(combined['Cabin'],prefix='Cabin')
        
        combined = pd.concat([combined,cabin_dummies],axis=1)
        
        combined.drop('Cabin',axis=1,inplace=True)
        
        self.status('cabin')
        return combined

    def process_sex(self, combined):
        
        # mapping string values to numerical one 
        combined['Sex'] = combined['Sex'].map({'male':1,'female':0})
        
        self.status('sex')

        return combined

    def process_pclass(self, combined):
        
        # encoding into 3 categories:
        pclass_dummies = pd.get_dummies(combined['Pclass'],prefix="Pclass")
        
        # adding dummy variables
        combined = pd.concat([combined,pclass_dummies],axis=1)
        
        # removing "Pclass"
        combined.drop('Pclass',axis=1,inplace=True)
        
        self.status('pclass')
        return combined

    def process_ticket(self, combined):
        
        # a function that extracts each prefix of the ticket, returns 'XXX' if no prefix (i.e the ticket is a digit)
        def cleanTicket(ticket):
            ticket = ticket.replace('.','')
            ticket = ticket.replace('/','')
            ticket = ticket.split()
            ticket = map(lambda t : t.strip() , ticket)
            ticket = list(filter(lambda t : not t.isdigit(), ticket))
            if len(ticket) > 0:
                return ticket[0]
            else: 
                return 'XXX'
        

        # Extracting dummy variables from tickets:

        combined['Ticket'] = combined['Ticket'].map(cleanTicket)
        tickets_dummies = pd.get_dummies(combined['Ticket'],prefix='Ticket')
        combined = pd.concat([combined, tickets_dummies],axis=1)
        combined.drop('Ticket',inplace=True,axis=1)

        self.status('ticket')
        return combined


    def process_family(self, combined):
        
        # introducing a new feature : the size of families (including the passenger)
        combined['FamilySize'] = combined['Parch'] + combined['SibSp'] + 1
        
        # introducing other features based on the family size
        combined['Singleton'] = combined['FamilySize'].map(lambda s : 1 if s == 1 else 0)
        combined['SmallFamily'] = combined['FamilySize'].map(lambda s : 1 if 2<=s<=4 else 0)
        combined['LargeFamily'] = combined['FamilySize'].map(lambda s : 1 if 5<=s else 0)
        
        self.status('family')
        return combined

    def scale_all_features(self, combined):
        
        features = list(combined.columns)
        features.remove('PassengerId')
        combined[features] = combined[features].apply(lambda x: x/x.max(), axis=0)
        
        print ('Features scaled successfully !')
        return combined

    def compute_score(self, clf, X, y,scoring='accuracy'):
        xval = cross_val_score(clf, X, y, cv = 5,scoring=scoring)
        return np.mean(xval)

    def get_normalized_data(self):

        self.combined = self.get_combined_data(self.train_file, self.test_file)

        print (self.combined.shape)
        print (self.combined.head(3))

        print(self.get_titles(self.combined))
        self.combined.head()

        grouped = self.combined.groupby(['Sex','Pclass','Title'])
        grouped.median()

        combined=self.process_age(self.combined)

        combined = self.process_names(combined)
        combined = self.process_fares(combined)
        combined = self.process_embarked(combined)
        combined = self.process_cabin(combined)
        combined = self.process_sex(combined)
        combined = self.process_pclass(combined)
        combined = self.process_ticket(combined)
        combined = self.process_family(combined)
        combined = self.scale_all_features(combined)

        return combined

def recover_train_test_target(train_file, combined):

    train0 = pd.read_csv(train_file)
    
    targets = train0.Survived
    train = combined.ix[0:890]
    test = combined.ix[891:]
    
    return train,test,targets

def save_result2(id, results,file):  

    this_file=open(file,'w')
    this_file.write("PassengerId,Survived\n")
    for i, v in zip(id, results):
        this_file.write(str(i)+","+str(v)+"\n")
    this_file.close()


@monitor_time
def extra_trees_classifier():

    tianic=Titanic_Data('../input/train.csv','../input/test.csv')

    combined_normalized_data=tianic.get_normalized_data()

    train,test,targets = recover_train_test_target('../input/train.csv', combined_normalized_data)

    
    clf = ExtraTreesClassifier(n_estimators=200)
    clf = clf.fit(train, targets)

    features = pd.DataFrame()
    features['feature'] = train.columns
    features['importance'] = clf.feature_importances_

    features.sort(['importance'],ascending=False)

    model = SelectFromModel(clf, prefit=True)
    train_new = model.transform(train)
    train_new.shape

    test_new = model.transform(test)
    test_new.shape

    forest = RandomForestClassifier(max_features='sqrt')

    parameter_grid = {
                     'max_depth' : [4,5,6,7,8],
                     'n_estimators': [200,210,240,250],
                     'criterion': ['gini','entropy']
                     }

    cross_validation = StratifiedKFold(targets, n_folds=5)

    grid_search = GridSearchCV(forest,
                               param_grid=parameter_grid,
                               cv=cross_validation)

    grid_search.fit(train_new, targets)

    print('Best score: {}'.format(grid_search.best_score_))
    print('Best parameters: {}'.format(grid_search.best_params_))

    output = grid_search.predict(test_new).astype(int)
    df_output = pd.DataFrame()
    df_output['PassengerId'] = test['PassengerId']
    df_output['Survived'] = output
    df_output[['PassengerId','Survived']].to_csv('./extra_trees_classifier_output.csv',index=False)

def keras_sequential_alcassifier():

    tianic=Titanic_Data('../input/train.csv','../input/test.csv')

    combined_normalized_data=tianic.get_normalized_data()

    train,test,targets = recover_train_test_target('../input/train.csv', combined_normalized_data)

    stdScaler = StandardScaler()
    X_train_scaled = stdScaler.fit_transform(train)
    X_test_scaled = stdScaler.transform(test)
    model = Sequential()
    #model.add(Dense(700, input_dim=7, init='normal', activation='relu'))
    #model.add(Dropout(0.5))
    model.add(Dense(1600, input_dim=68, init='normal', activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, init='normal', activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='rmsprop')
    model.fit(X_train_scaled, targets, nb_epoch=20, batch_size=32)

    result = model.predict(X_test_scaled)
    # rightnum = 0
    # for i in range(0, result.shape[0]):
    #     if result[i] >= 0.5:
    #         result[i] = 1
    #     else:
    #         result[i] = 0
    #     if result[i] == y_test.iloc[i]:
    #         rightnum += 1
    # print(rightnum/result.shape[0])

    # train_scaled = stdScaler.fit_transform(train[columns])
    # test_scaled = stdScaler.transform(test[columns])
    # model.fit(train_scaled, train['Survived'], nb_epoch=20, batch_size=32, verbose=0)
    # predict_NN = model.predict(test_scaled)
    # print(predict_NN.shape)
    # for i in range(0, predict_NN.shape[0]):
    #     if predict_NN[i] >= 0.5:
    #         predict_NN[i] = 1
    #     else:
    #         predict_NN[i] = 0
            
    # predict_NN = predict_NN.reshape((predict_NN.shape[0]))
    # predict_NN = predict_NN.astype('int')
    # print(predict_NN.shape)
    # submission = pd.DataFrame({
    #         "PassengerId": test["PassengerId"],
    #         "Survived": predict_NN
    #     })
    # submission.to_csv("titanic_predict_NN.csv", index=False)

    # test_results=model.predict(X_test_scaled, batch_size=200)
    # print test_results
    final=[]
    for i in result:
        if i>=0.5:
            final.append(1)
        else:
            final.append(0)

    save_result2(test['PassengerId'], final,'results_keras_sequential_neural_work.csv')



def main():
    # extra_trees_classifier()
    keras_sequential_alcassifier()
    
if __name__=="__main__":
    main()

        