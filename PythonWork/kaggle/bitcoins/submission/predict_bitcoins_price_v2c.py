#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import math
import os


# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
  dataX, dataY = [], []
  for i in range(len(dataset)-look_back):
    dataX.append(dataset[i])

    # print dataX, 'XXXXXXXXXXXXXXXXXX'
    dataY.append(dataset[i + look_back])
    # print dataY, 'YYYYYYYYYYYYYYYYYYYYYYY'
  return np.asarray(dataX), np.asarray(dataY)

# fix random seed for reproducibility
np.random.seed(9)

# load the dataset
df = read_csv('../input/bitcoin_price.csv', index_col="Date")

df = df.iloc[::-1]
print df.head()
df.index = pd.to_datetime(df.index)
df = df.sort_index(ascending=True)

print df.info()

df = df.drop(['Open','High','Low','Volume','Market Cap'], axis=1)
print df.columns

df.plot()
plt.ylabel("Daily Bitcoin price")
plt.show()


weekly=df.resample('W').sum()
weekly.plot()
plt.show()


dataset = df.values
dataset = dataset.astype('float32')

# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

#prepare the X and Y label
X,y = create_dataset(dataset, 1)

print X.shape, 'XXXXX', y.shape

#Take 80% of data as the training sample and 20% as testing sample
trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.20, shuffle=False)

print scaler.inverse_transform(trainX[:10])

# reshape input to be [samples, time steps, features]
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
print trainX[:3],trainX.shape, 'ttttttttttX'
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(4, input_shape=(1, 1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, nb_epoch=10, batch_size=1,  verbose=2)

#save model for later use
# model.save('./savedModel')
#load_model
# model = load_model('./savedModel')
# make predictions

trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

futurePredict = model.predict(np.asarray([[testPredict[-1]]]))
futurePredict = scaler.inverse_transform(futurePredict)

# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform(trainY)

testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform(testY)
print("Price for last 5 days: ")
print(testPredict[-5:])
print("Bitcoin price for tomorrow: ", futurePredict)

# calculate root mean squared error
trainScore = math.sqrt(mean_squared_error(trainY[:,0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[:,0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))

# shift train predictions for plotting
trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[1:len(trainPredict)+1, :] = trainPredict

# shift test predictions for plotting
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict):len(dataset)-1, :] = testPredict

# plot baseline and predictions
plt.plot(scaler.inverse_transform(dataset))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()