#PIPELINE
import cv2

import serial

import numpy as np
from keras.preprocessing import image

from keras.models import model_from_json
from keras.models import load_model


json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

loaded_model.load_weights("model.h5")
print("Loaded model from disk")



#Initialising our Arduino Inputs
arduinoData = serial.Serial('/dev/ttyACM0',9600)

# Playing video from file:
cap = cv2.VideoCapture(0)

#TO open text file
#f= open("SelfDrivingAuto.txt","w+")

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if(ret):
        
        inverted = cv2.flip( frame, 0 )
        k = cv2.waitKey(100)
        
        ysize = inverted.shape[0]
        xsize = inverted.shape[1]
        color_select = np.copy(inverted)

# Define color selection criteria
###### MODIFY THESE VARIABLES TO MAKE YOUR COLOR SELECTION
        red_threshold = 40
        green_threshold = 50
        blue_threshold = 50



        rgb_threshold = [red_threshold, green_threshold, blue_threshold]

# Do a boolean or with the "|" character to identify
# pixels below the thresholds
        thresholds = (inverted[:,:,0] < rgb_threshold[0]) \
                    | (inverted[:,:,1] < rgb_threshold[1]) \
                    | (inverted[:,:,2] < rgb_threshold[2])
        color_select[thresholds] = [0,0,0]

        
        
        ## use this
        '''test_image = image.load_img(inverted, target_size =(32,32))
        test_image = image.image_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        '''
        
        

        img = cv2.resize(color_select, (32,32))
        
        img = img.reshape(1, 32, 32, 3)
        cv2.imshow('frame',color_select)
       
        if(k == 82):
            break
        
        '''WE NEED INPUT FROM OUR TRAINED CNN MODEL'''
        output = loaded_model.predict_classes(img)
        print(output)
        
        if output == 0:
            arduinoData.write(str.encode('w'))
        elif output == 1:
            arduinoData.write(str.encode('a'))
        elif output == 2:
            arduinoData.write(str.encode('d'))
        elif output == 3:
            arduinoData.write(str.encode('z'))
        elif output == 4:
            arduinoData.write(str.encode('c'))
        
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
