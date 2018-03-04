#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from matplotlib.pylab import rcParams
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARIMA


data_price = pd.read_csv("../input/bitcoin_price.csv")
print data_price.head()

print data_price.shape
print data_price.isnull().sum()

print data_price.tail()


data_price_features_category=data_price.select_dtypes(include=['object']).columns
print data_price_features_category

data_price_features_numeric = data_price.select_dtypes(exclude=['object']).columns
print data_price_features_numeric



# data.index = pd.to_datetime(data_price.index)
# data = data_price.sort_index()
# data_price['Close'].plot()
# plt.ylabel("DAily Bitcoin price")
# plt.show()

# from statsmodels.tsa.arima_model import ARIMA

# ts_diff_logtrans = ts_diff_logtrans.fillna(0)
# model = ARIMA(ts_logtransformed, order=(8, 1, 0))  
# results_AR = model.fit(disp=-1)  
# plt.plot(ts_diff_logtrans)
# plt.plot(results_AR.fittedvalues, color='red', label = 'order 8')
# RSS = results_AR.fittedvalues-ts_diff_logtrans
# RSS.dropna(inplace=True)
# plt.title('RSS: %.4f'% sum(RSS**2))
# plt.legend(loc = 'best')

# df['date'] = pd.to_datetime(df['Date'],unit='s').dt.date
# group = df.groupby('Date')
# Real_Price = group['Weighted_Price'].mean()

# prediction_days = 30
# df_train= Real_Price[:len(Real_Price)-prediction_days]
# df_test= Real_Price[len(Real_Price)-prediction_days:]

# training_set = df_train.values
# training_set = np.reshape(training_set, (len(training_set), 1))
# from sklearn.preprocessing import MinMaxScaler
# sc = MinMaxScaler()
# training_set = sc.fit_transform(training_set)
# X_train = training_set[0:len(training_set)-1]
# y_train = training_set[1:len(training_set)]
# X_train = np.reshape(X_train, (len(X_train), 1, 1))


# from keras.models import Sequential
# from keras.layers import Dense
# from keras.layers import LSTM

# # Initialising the RNN
# regressor = Sequential()

# # Adding the input layer and the LSTM layer
# regressor.add(LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 1)))

# # Adding the output layer
# regressor.add(Dense(units = 1))

# # Compiling the RNN
# regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# # Fitting the RNN to the Training set
# regressor.fit(X_train, y_train, batch_size = 5, epochs = 100)


from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
import pandas as pd
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import plotly.offline as py
import plotly.graph_objs as go
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split



data = pd.read_csv(filepath_or_buffer="../input/bitcoin_price.csv", index_col="Date")
data.info()

data.index = pd.to_datetime(data.index)
data = data_price.sort_index(ascending=False)
print data.head(), '*********************'

data['Close'].plot()
plt.ylabel("DAily Bitcoin price")
plt.show()


from sklearn.preprocessing import MinMaxScaler
values = data['Close'].values.reshape(-1,1)
values = values.astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)



train_size = int(len(scaled) * 0.7)
test_size = len(scaled) - train_size
train, test = scaled[0:train_size,:], scaled[train_size:len(scaled),:]
print len(train), len(test)

def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back):
        a = dataset[i:(i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    print(len(dataY))
    return np.array(dataX), np.array(dataY)


look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
# X,y = create_dataset(scaled, look_back)
# trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.20)


trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

print trainX.shape[1],"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4"

print trainX.shape[2],"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4"
model = Sequential()
model.add(LSTM(100, input_shape=(trainX.shape[1], trainX.shape[2])))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
history = model.fit(trainX, trainY, nb_epoch=300, batch_size=100, validation_data=(testX, testY), verbose=0, shuffle=False)

pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()

yhat = model.predict(testX)
pyplot.plot(yhat, label='predict')
pyplot.plot(testY, label='true')
pyplot.legend()
pyplot.show()

yhat_train=model.predict(trainX)
yhat_train_inverse = scaler.inverse_transform(yhat_train.reshape(-1, 1))
trainY_inverse =  scaler.inverse_transform(trainY.reshape(-1, 1))


yhat_inverse = scaler.inverse_transform(yhat.reshape(-1, 1))
testY_inverse = scaler.inverse_transform(testY.reshape(-1, 1))

rmse_train=sqrt(mean_squared_error(trainY_inverse, yhat_train_inverse))
print ("Train RMSe:", rmse_train)


rmse = sqrt(mean_squared_error(testY_inverse, yhat_inverse))
print('Test RMSE: %.3f' % rmse)
print(testY_inverse[-5:]), "***************************************"

pyplot.plot(yhat_inverse, label='predict')
pyplot.plot(testY_inverse, label='actual', alpha=0.5)
pyplot.legend()
pyplot.show()


predictDates = data.tail(len(testX)).index
testY_reshape = testY_inverse.reshape(len(testY_inverse))
yhat_reshape = yhat_inverse.reshape(len(yhat_inverse))
actual_chart = go.Scatter(x=predictDates, y=testY_reshape, name= 'Actual Price')
predict_chart = go.Scatter(x=predictDates, y=yhat_reshape, name= 'Predict Price')
py.iplot([predict_chart, actual_chart])