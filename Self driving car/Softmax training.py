from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

from keras.models import model_from_json
from keras.models import load_model



#Initialising the CNN
classifier = Sequential()

#Adding convolution layers
classifier.add(Convolution2D(filters =32 , kernel_size = 3, input_shape = (32,32,3), activation = 'relu', padding = "valid"))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

#second convolutoin layer with pooling
classifier.add(Convolution2D(filters =32 , kernel_size = 3, activation = 'relu', padding = "valid"))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Convolution2D(filters =32 , kernel_size = 3, activation = 'relu', padding = "valid"))
classifier.add(MaxPooling2D(pool_size = (2, 2)))



#Flattening
classifier.add(Flatten())

#Full Connection
classifier.add(Dense(units= 128, activation = 'relu'))

classifier.add(Dense(units= 5, activation = 'softmax'))


#Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

#Fitting the cnn to the images
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'dataset1/training_set',
        target_size=(32, 32),
        batch_size=32,
        class_mode='categorical', 
        shuffle = True,
        )

test_set = test_datagen.flow_from_directory(
        'dataset1/test_set',
        target_size=(32, 32),
        batch_size=32,
        class_mode='categorical', 
        shuffle = True,
        )

#training the model finally
classifier.fit_generator(
        training_set,
        steps_per_epoch=500,
        epochs=25,
        validation_data=test_set,
        validation_steps=100)


training_set.class_indices


model_json = classifier.to_json()
with open("./model.json","w") as json_file:
  json_file.write(model_json)

classifier.save_weights("./model.h5")
print("saved model..! ready to go.")


import pickle
saved_model = pickle.dumps(classifier)