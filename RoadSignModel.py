import tensorflow as tf                          
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical          
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout

class RoadSignModel():

    def __init__(self, imageLoader):
        self.trained = False
        self.imageLoader = imageLoader
        self.model = Sequential()

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.imageLoader.get_images(), self.imageLoader.get_labels(), test_size=0.2, random_state=68)

        numberOfCategories = len(set(self.imageLoader.get_labels()))

        self.model.add(Conv2D(filters=32, kernel_size=(5,5), activation='relu', input_shape=X_train.shape[1:]))
        self.model.add(Conv2D(filters=32, kernel_size=(5,5), activation='relu'))
        self.model.add(MaxPool2D(pool_size=(2, 2)))
        self.model.add(Dropout(rate=0.25))
        self.model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
        self.model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
        self.model.add(MaxPool2D(pool_size=(2, 2)))
        self.model.add(Dropout(rate=0.25))
        self.model.add(Flatten())
        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dropout(rate=0.5))
        self.model.add(Dense(numberOfCategories, activation='softmax'))

        self.model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        history = self.model.fit(X_train, y_train, batch_size=32, epochs=2, validation_data=(X_test, y_test))

        self.trained = True

    def is_trained(self):

        return(self.trained)

    def save(self):
        self.model.save('model.h5')