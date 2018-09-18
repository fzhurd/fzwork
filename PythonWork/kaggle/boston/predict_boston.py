from sklearn.datasets import load_boston
import sklearn.datasets
import sklearn.ensemble
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, RandomForestRegressor

# to run the script
# python ./predict_boston.py

boston = load_boston()

rf = RandomForestRegressor(n_estimators=1000)

train, test, labels_train, labels_test = train_test_split(boston.data, boston.target, train_size=0.80)

rf.fit(train, labels_train)

RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=None,
           max_features='auto', max_leaf_nodes=None,
           min_impurity_split=1e-07, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           n_estimators=1000, n_jobs=1, oob_score=False, random_state=None,
           verbose=0, warm_start=False)

print('Random Forest MSError', np.mean((rf.predict(test) - labels_test) ** 2))

('Random Forest MSError', 17.349331324117653)

print('MSError when predicting the mean', np.mean((labels_train.mean() - labels_test) ** 2))

('MSError when predicting the mean', 79.186326166360075)

categorical_features = np.argwhere(np.array([len(set(boston.data[:,x])) for x in range(boston.data.shape[1])]) <= 10).flatten()

import lime
import lime.lime_tabular

explainer = lime.lime_tabular.LimeTabularExplainer(train, feature_names=boston.feature_names, class_names=['price'], categorical_features=categorical_features, verbose=True, mode='regression')
print type(boston.feature_names)
i = 25
exp = explainer.explain_instance(test[i], rf.predict, num_features=5)

print exp.show_in_notebook(show_table=True)

print exp.as_list()

