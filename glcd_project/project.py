import RPi.GPIO as GPIO
import time
import smtplib
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.IN) #PIR
GPIO.setup(24, GPIO.OUT) #BUzzer


try:
    #time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23)==1:
            GPIO.output(24, True)
            time.sleep(0.3) #Buzzer turns on for 0.5 sec
            GPIO.output(24, False)
            print("Motion Detected...")
            os.system('/home/pi/Desktop/pushbullet/pushbullet.sh "Alert Intruder"')
            time.sleep(0.5) #to avoid multiple detection
       
        else:
            
            GPIO.output(24,False)
            #time.sleep(0.01)
except:
    GPIO.cleanup()