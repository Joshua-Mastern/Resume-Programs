import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame

#set to True to enable debugging output
DEBUG = False

#initialize the pygame library
pygame.init()

#set GPIO pin numbers
#switches (from L TO R)
switches = [20, 16, 12, 26]
#leds (from L to R)
leds = [6, 13, 19, 21]
#sounds that map to each LED (From L to R)
sounds = [pygame.mixer.Sound("one.wav"),\
          pygame.mixer.Sound("two.wav"),\
          pygame.mixer.Sound("three.wav"),\
          pygame.mixer.Sound("four.wav")]

#use Broadcom pin mode
GPIO.setmode(GPIO.BCM)

#setup input and output pins
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

#turn LEDS on
def all_on():
    for i in leds:
        GPIO.output(leds, True)

#turn LEDS off
def all_off():
    for i in leds:
            GPIO.output(leds, False)


# flash LEDs a ferw times when the player loses the game
def lose():
    print "LOOOOOOOOOSER!!!!"
    if(len(seq) < 4):
        print "Wow you couldn't even get a single sequence right."
    else:
        temp = len(seq)-3
        print "You made it to round {}, remembering a total of {} leds.".format(temp, len(seq)-1)
        
    for i in range(0, 4):
        all_on()
        sleep(0.5)
        all_off()
        sleep(0.5)

################
# MAIN
################

# initialize the Simon sequence
# each item in  the sequence represents an LED (or switch)
# indexed at 0 through 3
seq = []
timeOnNote = 1
timeBetweenNote = 0.5
#randomly add the first two items to the sequence
seq.append(randint(0,3))
seq.append(randint(0,3))

print "Welcome to Simon!"
print "Try to play the sequence back by pressing the switches."
print "Press Ctrl+C to exit...."

#detect when Ctrl+c is pressed and reset GPIO pins
try:
    #continue until users presses Ctrl+C
    while(True):
        #randomly add one more item to the sequence
        seq.append(randint(0,3))
        if(DEBUG):
            #display the sequence
            if(len(seq) > 3):
                print
            print "seq = {}".format(seq)
        #adjust time depending on sequence
        if(len(seq)>= 5 and len(seq) < 7):
            timeOnNote = 0.9
            timeBetweenNote = 0.4
        elif(len(seq)>=7 and len(seq) < 10):
            timeOnNote = 0.8
            timeBetweenNote = 0.3
        elif(len(seq)>=10 and len(seq) < 13):
            timeOnNote = 0.7
            timeBetweenNote = 0.25
        elif(len(seq)>=13):
            timeOnNote = 0.6
            timeBetweenNote = 0.15
        print "Time on note: {}, Time between note: {}".format(timeOnNote, timeBetweenNote)
        # display the sequence using the LEDs
        for s in seq:
            if(len(seq) < 15):
                # turn on appropriate LED
                GPIO.output(leds[s], True)
            # play the corresponding sound
            sounds[s].play()
            sleep(timeOnNote)
            GPIO.output(leds[s], False)
            sleep(timeBetweenNote)

        # wait for player input (via switches)
        # initialize the count of switches pressed to 0
        switches_count = 0

        # keep accepting player input until the number of items in
        # the sequence is reached
        while(switches_count < len(seq)):
            # initialize note that no switch is pressed (helps with switch
            # debouncing)
            pressed = False
            # so long as no switch is currently pressed...
            while(not pressed):
                # ...check status of each switch
                for i in range(len(switches)):
                    # if one switch is pressed
                    while(GPIO.input(switches[i]) == True):
                        # note its index
                        val = i
                        # note that a switch has been pressed
                        pressed = True
            
            if(DEBUG):
                # display the index of the switch pressed
                print val,
            #light the matching LED
            GPIO.output(leds[val], True)
            # play its corresponding sound
            sounds[val].play()
            # wait and turn LED off again
            sleep(1)
            GPIO.output(leds[val], False)
            sleep(0.25)

            #check to see if LED is correct in the sequence
            if(val != seq[switches_count]):
                # player is incorrect, invoke lose function
                lose()
                #reset GPIO pins
                GPIO.cleanup()
                # exit the game
                exit(0)
            # if player has this item in the sequence correct,
            # increment the count
            switches_count += 1
# detect Ctrl+C
except KeyboardInterrupt:
    # reset GPIO.pins
    GPIO.cleanup()









                







