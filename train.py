import numpy as np
from scipy.fft import fft
from scipy.fft import fftfreq
from keras.models import Sequential
from keras.layers import Dropout
from keras.layers import Dense
from keras.layers import BatchNormalization
import matplotlib.pyplot as plt


data_x = np.array([])
for i in range(8000):
    f = open("dataset2/data/"+ str(i) +"_rand.txt", "r")
    rand = f.read()
    f.close()
    rand = np.array(list(rand), dtype=int)
    rand = fft(rand)
    data_x = np.append(data_x, rand, axis=0)



data_x = data_x.reshape((8000, 1024))



data_y = np.array([])

for i in range(8000):
    f = open("dataset2/label/"+ str(i) +"_lbl.txt", "r")
    lbl = f.read()
    f.close()
    lbl = float(lbl)
    data_y = np.append(data_y, lbl)



model = Sequential()
model.add(Dense(512, activation="relu", input_dim=1024))
model.add(Dense(256, activation="relu"))
model.add(Dense(128, activation="relu"))
#model.add(BatchNormalization())
model.add(Dense(1, activation="sigmoid"))

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mse'])

# Train the model
history = model.fit(data_x[:7000], data_y[:7000], epochs=50, shuffle=True, validation_split=0.2)



#rand = np.random.choice([0, 1], size=(200000))
#
#p_data = np.array([])
#text = ''
#for i in range(200000):
#    p = model.predict(fft(np.roll(rand, i)).reshape(1,200000))
#    text += str(int(p[0]))
#    print(i)
#
#
#f = open("result.txt", "w")
#
#f.write(text)
