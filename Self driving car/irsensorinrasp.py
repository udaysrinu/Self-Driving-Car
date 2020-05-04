
import RPi.GPIO as GPIO
import time

sensor1 = 16
sensor2 = 18
output=22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor1,GPIO.IN)
GPIO.setup(sensor2,GPIO.IN)
GPIO.setup(output,GPIO.OUT)

GPIO.output(output,False)
print ("IR Sensors Ready.....")
print (" ")

try: 
   while True:
      if not GPIO.input(sensor1) and  not GPIO.input(sensor2):
          GPIO.output(output,True)
          print ("black line Detected")
          while GPIO.input(sensor1) and GPIO.input(sensor2) :
              time.sleep(0.2)
      else:
          GPIO.output(output,False)
          print ("black line not Detected")


except KeyboardInterrupt:
    GPIO.cleanup()