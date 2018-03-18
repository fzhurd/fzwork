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
import seaborn as sns


# function to look_back one day earlier data
def create_dataset(dataset, look_back=1):
  dataX, dataY = [], []
  for i in range(len(dataset)-look_back):
    dataX.append(dataset[i])
    dataY.append(dataset[i + look_back])

  return np.asarray(dataX), np.asarray(dataY)

# function for preprocessing column, convert String to int
def convert_str_to_int(input_value):
    if input_value=='-':
        return 0
    else:
        return int(input_value.replace(',', ''))

# fix random seed for reproducibility
# np.random.seed(30)
np.random.seed(15)

# load the dataset
# df = read_csv('../input/bitcoin_price.csv', index_col="Date")
df = read_csv('../input/bitcoin_price_0316b.csv',index_col="Date")
# df = read_csv('../input/Book1.csv')

# sort the data from earliest to latest
df = df.iloc[::-1]
print df.head()

df.index = pd.to_datetime(df.index)
df = df.sort_index(ascending=True)

# covert two columns to int
# df['Volume']=df['Volume'].apply(convert_str_to_int)
# df['Market Cap']=df['Market Cap'].apply(convert_str_to_int)

print df.info()
print df.tail()

# plot the heatmap of correlation
sns.heatmap(df.corr(), annot=True, cmap='YlGnBu', linewidths=0.1)

# we only keep close price for analysis
df = df.drop(['Open','High','Low','Volume','Market Cap'], axis=1)
print df.columns

# plot the bitcoin price based on day
df.plot()
plt.ylabel("Daily Bitcoin price")
plt.show()

# plot the bitcoin price based on week
weekly=df.resample('W').sum()
weekly.plot()
plt.show()

# change close price to float
dataset = df.values
dataset = dataset.astype('float32')

# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

# prepare the X and Y label
X,y = create_dataset(dataset, 1)

# Take 80% of data as the training sample and 20% as testing sample
# Here we should NOT shuffle the data as it is based on the previous date
trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.20, shuffle=False)

print scaler.inverse_transform(trainX[:10])
print len(testY), 'testY length'

# reshape input to be [samples, time steps, features]
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(4, input_shape=(1, 1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
history=model.fit(trainX, trainY, nb_epoch=5, batch_size=1, validation_data=(testX, testY), verbose=2)

# plot the loss vs val_loss
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()

# predict the bitcoin price in train_predict and test_predict
train_predict = model.predict(trainX)
test_predict = model.predict(testX)

futurePredict = model.predict(np.asarray([[test_predict[-1]]]))
futurePredict = scaler.inverse_transform(futurePredict)

# invert predictions
train_predict = scaler.inverse_transform(train_predict)
trainY = scaler.inverse_transform(trainY)

test_predict = scaler.inverse_transform(test_predict)
testY = scaler.inverse_transform(testY)

print("Price for last 10 days: ")
print(test_predict[-10:])
print("Bitcoin price for tomorrow: ", futurePredict)
print ('test prdict length', len(test_predict))

# calculate root mean squared error
trainScore = math.sqrt(mean_squared_error(trainY[:,0], train_predict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[:,0], test_predict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))

# shift train predictions for plotting
train_predictPlot = np.empty_like(dataset)
train_predictPlot[:, :] = np.nan
train_predictPlot[1:len(train_predict)+1, :] = train_predict

# shift test predictions for plotting
test_predictPlot = np.empty_like(dataset)
test_predictPlot[:, :] = np.nan
test_predictPlot[len(train_predict):len(dataset)-1, :] = test_predict

# plot baseline and predictions
plt.plot(scaler.inverse_transform(dataset))
plt.plot(train_predictPlot)
plt.plot(test_predictPlot, alpha=0.5)
plt.show()