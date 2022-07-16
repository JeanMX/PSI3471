#cnn2.py - grad2020 - Testado em TF2 em Colab
import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
import tensorflow.keras as keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras import optimizers
from tensorflow.keras.callbacks import ReduceLROnPlateau
import numpy as np; import sys

def deslocaEsquerda(a):
    d=a.copy(); d[:,0:-1]=a[:,1:]; return d
def deslocaDireita(a):
    d=a.copy(); d[:,1:]=a[:,0:-1]; return d
def deslocaCima(a):
    d=a.copy(); d[0:-1,:]=a[1:,:]; return d
def deslocaBaixo(a):
    d=a.copy(); d[1:,:]=a[0:-1,:]; return d
print("Lendo MNIST")
(AX, AY), (QX, QY) = mnist.load_data()
AX=255-AX; QX=255-QX
print("Fazendo manualmente data augmentation")
AX.resize((5*60000,28,28))
AY.resize((5*60000,1))
for s in range(60000):
    AX[s+60000]=deslocaEsquerda(AX[s])
    AX[s+2*60000]=deslocaDireita(AX[s])
    AX[s+3*60000]=deslocaCima(AX[s])
    AX[s+4*60000]=deslocaBaixo(AX[s])
    AY[s+60000]=AY[s]
    AY[s+2*60000]=AY[s]
    AY[s+3*60000]=AY[s]
    AY[s+4*60000]=AY[s]

print("Convertendo para categorico e float")
nclasses = 10
AY2 = keras.utils.to_categorical(AY, nclasses)
QY2 = keras.utils.to_categorical(QY, nclasses)
nl, nc = AX.shape[1], AX.shape[2] #28, 28
AX = AX.astype('float32') / 255.0 - 0.5 # -0.5 a +0.5
QX = QX.astype('float32') / 255.0 - 0.5 # -0.5 a +0.5
AX = AX.reshape(AX.shape[0], nl, nc, 1)
QX = QX.reshape(QX.shape[0], nl, nc, 1)
print("Construindo modelo")
model = Sequential()
model.add(Conv2D(20, kernel_size=(3,3), activation='relu', input_shape=(nl,nc,1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(40, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(80, kernel_size=(3,3), activation='relu'))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(200, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(50, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(40, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(nclasses, activation='softmax'))
print("Treinando modelo")
opt=optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=["accuracy"])
reduce_lr = ReduceLROnPlateau(monitor='accuracy', factor=0.9, patience=2, min_lr=0.0001, verbose=True)
model.fit(AX, AY2, batch_size=1000, epochs=100, verbose=2, validation_data=(QX, QY2), callbacks=[reduce_lr])
score = model.evaluate(QX, QY2, verbose=False)
print('Test loss: %.4f'%(score[0]))
print('Test accuracy: %.2f %%'%(100*score[1]))
print('Test error: %.2f %%'%(100*(1-score[1])))
model.save("cnn2.h5")