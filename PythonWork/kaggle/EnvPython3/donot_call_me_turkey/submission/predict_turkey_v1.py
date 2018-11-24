#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from keras.preprocessing.sequence import pad_sequences
from keras.models import Model
from keras.layers import Dense, Dropout, Bidirectional, CuDNNGRU, Reshape, GlobalMaxPooling1D, GlobalAveragePooling1D, Input, concatenate, BatchNormalization
from keras.optimizers import Adam


data=pd.read_json("../input/train.json")
print (data.head())
print (data.shape)
print (data.isnull().sum())

print (data.info)

print (data['is_turkey'].head(20))
df_test = pd.read_json('../input/test.json')

# print (data.columns)

features= ['audio_embedding', 'end_time_seconds_youtube_clip', 'is_turkey',
       'start_time_seconds_youtube_clip', 'vid_id']

y = data['is_turkey']
X = data.drop(['is_turkey'], axis=1)
print (X.columns)

max_len = 10
feature_size = 128

# X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3)

# rf_model=RandomForestClassifier()
# rf_model.fit(X_train, y_train)
# predicted = rf_model.predict(X_test)

# print (accuracy_score(predicted, y_test))

df_train=data

X = pad_sequences(df_train['audio_embedding'], maxlen=10, padding='post')
X_test = pad_sequences(df_test['audio_embedding'], maxlen=10, padding='post')

y = df_train['is_turkey'].values

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

def build_model():
    inp = Input(shape=(max_len, feature_size))
    x = BatchNormalization()(inp)
    # x = Bidirectional(CuDNNGRU(256, return_sequences=True))(x)
    # x = Bidirectional(CuDNNGRU(128, return_sequences=True))(x)
    avg_pool = GlobalAveragePooling1D()(x)
    max_pool = GlobalMaxPooling1D()(x)
    concat = concatenate([avg_pool, max_pool])
    concat = Dense(64, activation="relu")(concat)
    concat = Dropout(0.5)(concat)
    output = Dense(1, activation="sigmoid")(concat)
    model = Model(inputs=inp, outputs=output)
    model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.0001), metrics=['accuracy'])
    # model.compile(optimizer=Adam(lr=0.0001), metrics=['accuracy'])
    return model

model = build_model()

from keras.callbacks import ReduceLROnPlateau

reduce_lr = ReduceLROnPlateau(monitor='val_acc', factor=0.1, patience=2, verbose=1, min_lr=1e-8)

epochs = 20

# history = model.fit(X_train, y_train, batch_size=256, epochs=epochs, validation_data=[X_val, y_val], callbacks=[reduce_lr], verbose=2)
history = model.fit(X_train, y_train, batch_size=256, epochs=epochs, validation_data=[X_val, y_val], callbacks=[reduce_lr], verbose=2)
from sklearn.metrics import accuracy_score

val = model.evaluate(X_val, y_val, verbose=1)
print("Accuracy on validation data : ", val[1])

model_final = build_model()
reduce_lr_final = ReduceLROnPlateau(monitor='acc', factor=0.1, patience=2, verbose=1, min_lr=1e-8)

model_final.fit(X, y, epochs=10, batch_size=256, verbose=2, callbacks=[reduce_lr_final])

y_test = model_final.predict(X_test, verbose=1)
submission = pd.DataFrame({'vid_id': df_test['vid_id'].values, 'is_turkey': list(y_test.flatten())})

submission.head()

submission.to_csv("submission.csv", index=False)

