from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.utils import np_utils

import wandb
from wandb.wandb_keras import WandbKerasCallback

# logging code
run = wandb.init()
config = run.config

# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

is_five_train = y_train == 5
is_five_test = y_test == 5

img_width = X_train.shape[1]
img_height = X_train.shape[2]

# create model
model=Sequential()
model.add(Flatten(input_shape=(img_width,img_height)))
model.add(Dense(1, activation="sigmoid"))
model.compile(loss='mse', optimizer='adam',
                metrics=['binary_accuracy'])

# Fit the model
model.fit(X_train, is_five_train, epochs=10, validation_data=(X_test, is_five_test),
                    callbacks=[WandbKerasCallback()])

print(model.predict(X_train[:10]))
