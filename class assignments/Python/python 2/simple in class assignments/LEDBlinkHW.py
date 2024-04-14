###############################################################################
# Name: Joshua Brack
# Date: 10/17/2018
# Description: Led blinks at 0.5 seconds on and off unless switch is pressed.
# Then it blinks at 0.1 seconds on and off.
###############################################################################
#import needed files
import RPi.GPIO as GPIO
from time import sleep

#Declare gpio modes and pins
led = 17
button = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#loop repeating forever
while(True):
    #if switch is open blink on and off at 0.5 sec rate
    if (GPIO.input(button) == GPIO.LOW):
        GPIO.output(17, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(17, GPIO.LOW)
        sleep(0.5)
    #else blink at rate of 0.1sec
    elif (GPIO.input(button) == GPIO.HIGH):
        GPIO.output(17, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(17, GPIO.LOW)
        sleep(0.1)
