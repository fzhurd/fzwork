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

    combined=[]
    data=None

    def __init__(self, train_file, test_file):

        this.train_file = train_file
        this.test_file=test_file

        self.preprocess(train_file)

    def preprocess(self, file)

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


    def status(self, train_file,test_file, feature):

        print ('Processing',feature,': ok')


    def get_combined_data(self, train_file, test_file):

        # global combined
        train = pd.read_csv(train_file)
        
        # reading test data
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

        # global combined
        
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
        
        # global combined
        
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
        
        # global combined
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
        
        # global combined
        # there's one missing fare value - replacing it with the mean.
        combined.Fare.fillna(combined.Fare.mean(),inplace=True)
        
        self.status('fare')
        return combined



    def process_embarked(self, combined):
        
        # global combined
        # two missing embarked values - filling them with the most frequent one (S)
        combined.Embarked.fillna('S',inplace=True)
        
        # dummy encoding 
        embarked_dummies = pd.get_dummies(combined['Embarked'],prefix='Embarked')
        combined = pd.concat([combined,embarked_dummies],axis=1)
        combined.drop('Embarked',axis=1,inplace=True)
        
        self.status('embarked')

        return combined



    def process_cabin(self, combined):
        
        # global combined
        
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
        
        # global combined
        # mapping string values to numerical one 
        combined['Sex'] = combined['Sex'].map({'male':1,'female':0})
        
        self.status('sex')

        return combined

    def process_pclass(self, combined):
        
        # global combined
        # encoding into 3 categories:
        pclass_dummies = pd.get_dummies(combined['Pclass'],prefix="Pclass")
        
        # adding dummy variables
        combined = pd.concat([combined,pclass_dummies],axis=1)
        
        # removing "Pclass"
        
        combined.drop('Pclass',axis=1,inplace=True)
        
        self.status('pclass')

        return combined

    def process_ticket(self, combined):
        
        # global combined
        
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
        
        # global combined
        # introducing a new feature : the size of families (including the passenger)
        combined['FamilySize'] = combined['Parch'] + combined['SibSp'] + 1
        
        # introducing other features based on the family size
        combined['Singleton'] = combined['FamilySize'].map(lambda s : 1 if s == 1 else 0)
        combined['SmallFamily'] = combined['FamilySize'].map(lambda s : 1 if 2<=s<=4 else 0)
        combined['LargeFamily'] = combined['FamilySize'].map(lambda s : 1 if 5<=s else 0)
        
        self.status('family')

        return combined

    def scale_all_features(self, combined):
        
        # global combined
        
        features = list(combined.columns)
        features.remove('PassengerId')
        combined[features] = combined[features].apply(lambda x: x/x.max(), axis=0)
        
        print ('Features scaled successfully !')

        return combined

    def compute_score(self, clf, X, y,scoring='accuracy'):
        xval = cross_val_score(clf, X, y, cv = 5,scoring=scoring)
        return np.mean(xval)

    def recover_train_test_target(self, train_file):
        # global combined
        
        train0 = pd.read_csv(train_file)
        
        targets = train0.Survived
        train = combined.ix[0:890]
        test = combined.ix[891:]
        
        return train,test,targets

    def get_normalized_data(self):

        self.combined = self.get_combined_data(self.train_data, self.test_data)
        print (self.combined.shape)
        print (self.combined.head(3))

        print(self.get_titles())
        self.combined.head()

        grouped = combined.groupby(['Sex','Pclass','Title'])
        grouped.median()

        self.process_age()
        combined.info()

        self.process_names()
        self.process_fares()
        self.self.process_embarked()
        self.self.process_cabin()
        self.process_sex()
        self.process_pclass()
        self.process_ticket()
        self.process_family()
        self.scale_all_features()

        return combined

def extra_trees_classifier():

    tianic=Titanic_Data('../input/train.csv','../input/test.csv')
    combined_normalized_data=titanic.get_normalized_data()

    train,test,targets = tianic.recover_train_test_target()

    
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
    df_output[['PassengerId','Survived']].to_csv('./output.csv',index=False)

@monitor_time
def main():
    extra_trees_classifier()
    # data = pd.read_csv('../input/train.csv')
    # print (data.head(5))

    # data['Age'].fillna(data['Age'].median(), inplace=True)

    # survived_sex = data[data['Survived']==1]['Sex'].value_counts()
    # dead_sex = data[data['Survived']==0]['Sex'].value_counts()
    # df = pd.DataFrame([survived_sex,dead_sex])
    # df.index = ['Survived','Dead']
    # df.plot(kind='bar',stacked=True, figsize=(15,8))


    # survived_embark = data[data['Survived']==1]['Embarked'].value_counts()
    # dead_embark = data[data['Survived']==0]['Embarked'].value_counts()
    # df = pd.DataFrame([survived_embark,dead_embark])
    # df.index = ['Survived','Dead']
    # df.plot(kind='bar',stacked=True, figsize=(15,8))



    # combined = get_combined_data()
    # print (combined.shape)
    # print (combined.head(3))

    # print(get_titles())
    # combined.head()

    # grouped = combined.groupby(['Sex','Pclass','Title'])
    # grouped.median()

    # process_age()
    # combined.info()

    # process_names()
    # process_fares()
    # process_embarked()
    # process_cabin()
    # process_sex()
    # process_pclass()
    # process_ticket()
    # process_family()
    # scale_all_features()



    # train,test,targets = recover_train_test_target()

    
    # clf = ExtraTreesClassifier(n_estimators=200)
    # clf = clf.fit(train, targets)

    # features = pd.DataFrame()
    # features['feature'] = train.columns
    # features['importance'] = clf.feature_importances_

    # features.sort(['importance'],ascending=False)

    # model = SelectFromModel(clf, prefit=True)
    # train_new = model.transform(train)
    # train_new.shape

    # test_new = model.transform(test)
    # test_new.shape

    # forest = RandomForestClassifier(max_features='sqrt')

    # parameter_grid = {
    #                  'max_depth' : [4,5,6,7,8],
    #                  'n_estimators': [200,210,240,250],
    #                  'criterion': ['gini','entropy']
    #                  }

    # cross_validation = StratifiedKFold(targets, n_folds=5)

    # grid_search = GridSearchCV(forest,
    #                            param_grid=parameter_grid,
    #                            cv=cross_validation)

    # grid_search.fit(train_new, targets)

    # print('Best score: {}'.format(grid_search.best_score_))
    # print('Best parameters: {}'.format(grid_search.best_params_))

    # output = grid_search.predict(test_new).astype(int)
    # df_output = pd.DataFrame()
    # df_output['PassengerId'] = test['PassengerId']
    # df_output['Survived'] = output
    # df_output[['PassengerId','Survived']].to_csv('./output.csv',index=False)

if __name__=="__main__":
    main()

        

# def monitor_time(func):

#     @wraps(func)
#     def calculate_time(*args, **kwargs ):
#         start_time = time.time()
#         result=func(*args, **kwargs)
#         end_time=time.time()
#         cost_time=end_time-start_time
#         print(cost_time)
#         return result

#     return calculate_time


# pd.options.display.max_columns = 100
# pd.options.display.max_rows = 100
# combined=[]

# def status(feature):
#     print ('Processing',feature,': ok')

# def get_combined_data():

#     global combined
#     train = pd.read_csv('../input/train.csv')
    
#     # reading test data
#     test = pd.read_csv('../input/test.csv')

#     # extracting and then removing the targets from the training data 
#     targets = train.Survived
#     train.drop('Survived',1,inplace=True)
    

#     # merging train data and test data for future feature engineering
#     combined = train.append(test)
#     combined.reset_index(inplace=True)
#     combined.drop('index',inplace=True,axis=1)
    
#     return combined

# def get_titles():

#     global combined
    
#     # we extract the title from each name
#     combined['Title'] = combined['Name'].map(lambda name:name.split(',')[1].split('.')[0].strip())
    
#     # a map of more aggregated titles
#     Title_Dictionary = {
#                         "Capt":       "Officer",
#                         "Col":        "Officer",
#                         "Major":      "Officer",
#                         "Jonkheer":   "Royalty",
#                         "Don":        "Royalty",
#                         "Sir" :       "Royalty",
#                         "Dr":         "Officer",
#                         "Rev":        "Officer",
#                         "the Countess":"Royalty",
#                         "Dona":       "Royalty",
#                         "Mme":        "Mrs",
#                         "Mlle":       "Miss",
#                         "Ms":         "Mrs",
#                         "Mr" :        "Mr",
#                         "Mrs" :       "Mrs",
#                         "Miss" :      "Miss",
#                         "Master" :    "Master",
#                         "Lady" :      "Royalty"

#                         }
    
#     # we map each title
#     combined['Title'] = combined.Title.map(Title_Dictionary)

# def process_age():
    
#     global combined
    
#     # a function that fills the missing values of the Age variable
    
#     def fillAges(row):
#         if row['Sex']=='female' and row['Pclass'] == 1:
#             if row['Title'] == 'Miss':
#                 return 30
#             elif row['Title'] == 'Mrs':
#                 return 45
#             elif row['Title'] == 'Officer':
#                 return 49
#             elif row['Title'] == 'Royalty':
#                 return 39

#         elif row['Sex']=='female' and row['Pclass'] == 2:
#             if row['Title'] == 'Miss':
#                 return 20
#             elif row['Title'] == 'Mrs':
#                 return 30

#         elif row['Sex']=='female' and row['Pclass'] == 3:
#             if row['Title'] == 'Miss':
#                 return 18
#             elif row['Title'] == 'Mrs':
#                 return 31

#         elif row['Sex']=='male' and row['Pclass'] == 1:
#             if row['Title'] == 'Master':
#                 return 6
#             elif row['Title'] == 'Mr':
#                 return 41.5
#             elif row['Title'] == 'Officer':
#                 return 52
#             elif row['Title'] == 'Royalty':
#                 return 40

#         elif row['Sex']=='male' and row['Pclass'] == 2:
#             if row['Title'] == 'Master':
#                 return 2
#             elif row['Title'] == 'Mr':
#                 return 30
#             elif row['Title'] == 'Officer':
#                 return 41.5

#         elif row['Sex']=='male' and row['Pclass'] == 3:
#             if row['Title'] == 'Master':
#                 return 6
#             elif row['Title'] == 'Mr':
#                 return 26
    
#     combined.Age = combined.apply(lambda r : fillAges(r) if np.isnan(r['Age']) else r['Age'], axis=1)
    
#     status('age')

# def process_names():
    
#     global combined
#     # we clean the Name variable
#     combined.drop('Name',axis=1,inplace=True)
    
#     # encoding in dummy variable
#     titles_dummies = pd.get_dummies(combined['Title'],prefix='Title')
#     combined = pd.concat([combined,titles_dummies],axis=1)
    
#     # removing the title variable
#     combined.drop('Title',axis=1,inplace=True)
    
#     status('names')

# def process_fares():
    
#     global combined
#     # there's one missing fare value - replacing it with the mean.
#     combined.Fare.fillna(combined.Fare.mean(),inplace=True)
    
#     status('fare')



# def process_embarked():
    
#     global combined
#     # two missing embarked values - filling them with the most frequent one (S)
#     combined.Embarked.fillna('S',inplace=True)
    
#     # dummy encoding 
#     embarked_dummies = pd.get_dummies(combined['Embarked'],prefix='Embarked')
#     combined = pd.concat([combined,embarked_dummies],axis=1)
#     combined.drop('Embarked',axis=1,inplace=True)
    
#     status('embarked')



# def process_cabin():
    
#     global combined
    
#     # replacing missing cabins with U (for Uknown)
#     combined.Cabin.fillna('U',inplace=True)
    
#     # mapping each Cabin value with the cabin letter
#     combined['Cabin'] = combined['Cabin'].map(lambda c : c[0])
    
#     # dummy encoding ...
#     cabin_dummies = pd.get_dummies(combined['Cabin'],prefix='Cabin')
    
#     combined = pd.concat([combined,cabin_dummies],axis=1)
    
#     combined.drop('Cabin',axis=1,inplace=True)
    
#     status('cabin')

# def process_sex():
    
#     global combined
#     # mapping string values to numerical one 
#     combined['Sex'] = combined['Sex'].map({'male':1,'female':0})
    
#     status('sex')

# def process_pclass():
    
#     global combined
#     # encoding into 3 categories:
#     pclass_dummies = pd.get_dummies(combined['Pclass'],prefix="Pclass")
    
#     # adding dummy variables
#     combined = pd.concat([combined,pclass_dummies],axis=1)
    
#     # removing "Pclass"
    
#     combined.drop('Pclass',axis=1,inplace=True)
    
#     status('pclass')

# def process_ticket():
    
#     global combined
    
#     # a function that extracts each prefix of the ticket, returns 'XXX' if no prefix (i.e the ticket is a digit)
#     def cleanTicket(ticket):
#         ticket = ticket.replace('.','')
#         ticket = ticket.replace('/','')
#         ticket = ticket.split()
#         ticket = map(lambda t : t.strip() , ticket)
#         ticket = list(filter(lambda t : not t.isdigit(), ticket))
#         if len(ticket) > 0:
#             return ticket[0]
#         else: 
#             return 'XXX'
    

#     # Extracting dummy variables from tickets:

#     combined['Ticket'] = combined['Ticket'].map(cleanTicket)
#     tickets_dummies = pd.get_dummies(combined['Ticket'],prefix='Ticket')
#     combined = pd.concat([combined, tickets_dummies],axis=1)
#     combined.drop('Ticket',inplace=True,axis=1)

#     status('ticket')


# def process_family():
    
#     global combined
#     # introducing a new feature : the size of families (including the passenger)
#     combined['FamilySize'] = combined['Parch'] + combined['SibSp'] + 1
    
#     # introducing other features based on the family size
#     combined['Singleton'] = combined['FamilySize'].map(lambda s : 1 if s == 1 else 0)
#     combined['SmallFamily'] = combined['FamilySize'].map(lambda s : 1 if 2<=s<=4 else 0)
#     combined['LargeFamily'] = combined['FamilySize'].map(lambda s : 1 if 5<=s else 0)
    
#     status('family')

# def scale_all_features():
    
#     global combined
    
#     features = list(combined.columns)
#     features.remove('PassengerId')
#     combined[features] = combined[features].apply(lambda x: x/x.max(), axis=0)
    
#     print ('Features scaled successfully !')

# def compute_score(clf, X, y,scoring='accuracy'):
#     xval = cross_val_score(clf, X, y, cv = 5,scoring=scoring)
#     return np.mean(xval)

# def recover_train_test_target():
#     global combined
    
#     train0 = pd.read_csv('../input/train.csv')
    
#     targets = train0.Survived
#     train = combined.ix[0:890]
#     test = combined.ix[891:]
    
#     return train,test,targets

# @monitor_time
# def main():
#     data = pd.read_csv('../input/train.csv')
#     print (data.head(5))

#     data['Age'].fillna(data['Age'].median(), inplace=True)

#     survived_sex = data[data['Survived']==1]['Sex'].value_counts()
#     dead_sex = data[data['Survived']==0]['Sex'].value_counts()
#     df = pd.DataFrame([survived_sex,dead_sex])
#     df.index = ['Survived','Dead']
#     df.plot(kind='bar',stacked=True, figsize=(15,8))


#     survived_embark = data[data['Survived']==1]['Embarked'].value_counts()
#     dead_embark = data[data['Survived']==0]['Embarked'].value_counts()
#     df = pd.DataFrame([survived_embark,dead_embark])
#     df.index = ['Survived','Dead']
#     df.plot(kind='bar',stacked=True, figsize=(15,8))



#     combined = get_combined_data()
#     print (combined.shape)
#     print (combined.head(3))

#     print(get_titles())
#     combined.head()

#     grouped = combined.groupby(['Sex','Pclass','Title'])
#     grouped.median()

#     process_age()
#     combined.info()

#     process_names()
#     process_fares()
#     process_embarked()
#     process_cabin()
#     process_sex()
#     process_pclass()
#     process_ticket()
#     process_family()
#     scale_all_features()

#     train,test,targets = recover_train_test_target()

    
#     clf = ExtraTreesClassifier(n_estimators=200)
#     clf = clf.fit(train, targets)

#     features = pd.DataFrame()
#     features['feature'] = train.columns
#     features['importance'] = clf.feature_importances_

#     features.sort(['importance'],ascending=False)

#     model = SelectFromModel(clf, prefit=True)
#     train_new = model.transform(train)
#     train_new.shape

#     test_new = model.transform(test)
#     test_new.shape

#     forest = RandomForestClassifier(max_features='sqrt')

#     parameter_grid = {
#                      'max_depth' : [4,5,6,7,8],
#                      'n_estimators': [200,210,240,250],
#                      'criterion': ['gini','entropy']
#                      }

#     cross_validation = StratifiedKFold(targets, n_folds=5)

#     grid_search = GridSearchCV(forest,
#                                param_grid=parameter_grid,
#                                cv=cross_validation)

#     grid_search.fit(train_new, targets)

#     print('Best score: {}'.format(grid_search.best_score_))
#     print('Best parameters: {}'.format(grid_search.best_params_))

#     output = grid_search.predict(test_new).astype(int)
#     df_output = pd.DataFrame()
#     df_output['PassengerId'] = test['PassengerId']
#     df_output['Survived'] = output
#     df_output[['PassengerId','Survived']].to_csv('./output.csv',index=False)



# if __name__=="__main__":
#     main()