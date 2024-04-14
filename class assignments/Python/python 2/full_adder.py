import RPi.GPIO as GPIO
from time import sleep
# set the GPIO pin numbers
inA = 25
inB = 5
outS = 17
outC = 22
# use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)
# setup the input and output pins
GPIO.setup(inA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(inB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(outS, GPIO.OUT)
GPIO.setup(outC, GPIO.OUT)
# we'll discuss this later, but the try-except construct allows
# us to detect when Ctrl+C is pressed so that we can reset the
# GPIO pins
try:
    # keep going until the user presses Ctrl+C
    while (True):
        # initialize A, B, S, and C
        A = 0
        B = 0
        S = 0
        C = 0
        # set A and B depending on the switches
        if (GPIO.input(inA) == GPIO.HIGH):
        A = 1
        if (GPIO.input(inB) == GPIO.HIGH):
        B = 1
        # calculate S and C using A and B
        S = A ^ B # A xor B
        8
        C = A & B # A and B
        # set the output pins appropriately
        # (to light the LEDs as appropriate)
        GPIO.output(outS, S)
        GPIO.output(outC, C)
        # detect Ctrl+C
except KeyboardInterrupt:
    # reset the GPIO pins
    GPIO.cleanup()

