#PIPELINEw
import cv2
import os
import serial
import matplotlib.pyplot as plt
import numpy as np
import time


arduinoData = serial.Serial('/dev/ttyACM0',9600)
# Playing video from file:
cap = cv2.VideoCapture(0)

try:
    if not os.path.exists('data3'):
        print("hello")
        os.makedirs('data3')
        os.makedirs('data3/front/')
        os.makedirs('data3/left/')
        os.makedirs('data3/right/')
        os.makedirs('data3/steepleft/')
        os.makedirs('data3/steepright/')
        os.makedirs('data3/stopsign/')
        os.makedirs('data3/no_crossing/')
        os.makedirs('data3/end/')
except OSError:
    print ('Error: Creating directory of data')
k = 119
currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret :
        # To stop duplicate images
        currentFrame += 1
        inverted = cv2.flip( frame, 0 )
        
        
       
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

# Display the image                 


        cv2.imshow('final frame', color_select)
    
        x = cv2.waitKey(50)
        
        if(x == 255):
            key = k
            # Saves image of the current frame in jpg file 
            if(key == 97):
                arduinoData.write(str.encode('a'))
                name = './data3/left/frame' + str(currentFrame) + '_1l.jpg'
                print ('Creating...' + name)
                cv2.imwrite(name, color_select)
                
            
                
                # Sves image of the current frame in jpg file 
            elif(key == 100):
                arduinoData.write(str.encode('d'))
                name = './data3/right/frame' + str(currentFrame) + '_1r.jpg'
                print ('Creating...' + name)
                cv2.imwrite(name, color_select)
                
            elif(key == 111): 
                arduinoData.write(str.encode('s'))
                break
                    
            elif (key == 119):
                arduinoData.write(str.encode('w'))
                name = './data3/front/frame' + str(currentFrame) + '_1f.jpg'
                print ('Creating...' + name)
                cv2.imwrite(name,color_select)
                
            
            elif(key == 115):
                arduinoData.write(str.encode('s'))
                print('stop')
            
            elif(key == 122):
                
                arduinoData.write(str.encode('z'))
                name = './data3/steepleft/frame' + str(currentFrame) + '___1_sl.jpg'
                print ('Creating...' + name)
                cv2.imwrite(name, color_select)
                
            elif(key == 99):
                arduinoData.write(str.encode('c'))
                name = './data3/steepright/frame' + str(currentFrame) + '___1_sr.jpg'
                print ('Creating...' + name)
                cv2.imwrite(name, color_select)
            elif(key == 110 ):
                name = './data3/no_crossing/frame' + str(currentFrame) + 'no_crossing.jpg'
                print ('Creating...' + name)
            elif(key == 32):
                name = './data3/stopsign/frame' + str(currentFrame) + 'stopsign.jpg'
                print ('Creating...' + name)
            elif(key == 105):
                name = './data3/end/frame' + str(currentFrame) + 'end.jpg'
                print ('Creating...' + name)
                arduinoData.write(str.encode('s'))
                #f.write("%c\r\n" % (x))
                
        else:
            key = x
            k = x
            
                
                #f.write("%c\r\n" % ('f'))

    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()