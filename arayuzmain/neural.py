import tensorflow as tf
from sklearn.model_selection import train_test_split
import numpy as np
from random import random
import pandas as pd 
import os
import joblib

data = pd.read_csv("chartlab1405.csv")
data = data.sample(frac = 1)

data.drop("SUBJECT_ID",axis=1,inplace=True)
data.drop("SEQ_NUM",axis=1,inplace=True)
data.drop("CHARTTIME",axis=1,inplace=True)
data.drop("VALUEUOM",axis=1,inplace=True)

from sklearn.preprocessing import OneHotEncoder

#creating instance of one-hot-encoder
encoder = OneHotEncoder(handle_unknown='ignore')

#perform one-hot encoding on 'team' column 
encoder_df = pd.DataFrame(encoder.fit_transform(data[['CLASSLABEL']]).toarray())

#merge one-hot encoded columns back with original DataFrame
final_df = data.join(encoder_df)

final_df.drop('CLASSLABEL', axis=1, inplace=True)

cols = [4,5,6,7]
labels = final_df[final_df.columns[cols]]

data = final_df

data.drop(0, axis=1, inplace=True)
data.drop(1,axis=1,inplace=True)
data.drop(2,axis=1,inplace=True)
data.drop(3,axis=1,inplace=True)

x_train,x_test,y_train,y_test = train_test_split(data,labels)

print(type(x_train)) 
print(type(y_train))


y_train = y_train.values.astype(np.float32)

y_test = y_test.values.astype(np.float32)

x_train = x_train.values.astype(np.float32)

x_test = x_test.values.astype(np.float32)

model = tf.keras.models.Sequential([
                                    
      tf.keras.layers.Dense(32, input_dim=4, activation="tanh"),
      
      tf.keras.layers.Dense(16, activation="relu"),
      tf.keras.layers.Dropout(0.4),

      tf.keras.layers.Dense(16, activation="relu"),
      tf.keras.layers.Dropout(0.4),

      tf.keras.layers.Dense(12, activation="relu"),
   

      tf.keras.layers.Dense(4, activation="softmax")
    ])

# choose optimiser
optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

opt = tf.keras.optimizers.Adam(learning_rate=0.01)

# compile model
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy','categorical_accuracy'])

# train model
model.fit(x_train, y_train, validation_split = 0.1, epochs=1)

model.save('./models')