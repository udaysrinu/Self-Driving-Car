#PIPELINE
import cv2
import os
import serial
import matplotlib.pyplot as plt
import numpy as np

#arduinoData = serial.Serial('/dev/ttyACM0',9600)
# Playing video from file:
cap = cv2.VideoCapture(0)


currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    key = cv2.waitKey(100)
    if ret :
        # To stop duplicate images
        cv2.imshow('fraME', frame)
        print(key)