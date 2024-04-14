##################################################################
#Name: Joshua Brack
#Date: 6/5/2019
#Description: Piano keys that are different formas of C.
#               Also draws these different forms
##################################################################



import RPi.GPIO as GPIO
from time import sleep
import pygame
from array import array
from waveform_vis import WaveformVis

MIXER_FREQ= 44100
MIXER_SIZE = -16
MIXER_CHANS = 1
MIXER_BUFF = 1024

DEBUG = True

class Note(pygame.mixer.Sound):
    def __init__(self, frequency, volume, waveName):
        self.frequency = frequency
        self.waveName = waveName
        pygame.mixer.Sound.__init__(self, buffer = self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) -1) - 1
        samples = array("h", [0] * period)

        if (self.waveName == "square"):
            for t in range(period):
                #the first half of the period is positive
                if (t < period/2):
                    samples[t] = amplitude
                #second half is negative
                elif(t >= period/2):
                    samples[t] = -amplitude

        if (self.waveName == "triangle"):
            for t in range(period):
                if ((t < period/4) and ((4*amplitude)/period)*t <= 32767):
                    samples[t] = ((4*amplitude)/period)*t
                elif ((t < period/4) and ((4*amplitude)/period)*t > 32767):
                    samples[t] = 32767
                elif (((period/4) < t < (3*period/4)) and ((-4*amplitude)/period)*t + amplitude <= 32767):
                    samples[t] = ((-(4*amplitude)/period)*t + 2*amplitude)
                elif (((period/4) < t < (3*period/4)) and ((((-4*amplitude)/period)*t + amplitude) > 32767)):
                    samples[t] = 32767
                elif (((3*period/4) < t) and ((4*amplitude)/period)*t - 4*amplitude >= -32768):
                    samples[t] = ((4*amplitude)/period)*t - 4*amplitude
                elif (((3*period/4) < t) and ((4*amplitude)/period)*t - 4*amplitude < -32768):
                    samples[t] = -32768

        if (self.waveName == "sinusoidal"):
            for t in range(period):
                #first half
                if (t < period/2):
                    samples[t] = -18*(t-period/4)**2 + amplitude
                #second half
                elif (t >= period/2):
                    samples[t] = 18*(t-(3*period/4))**2 - amplitude
                    
        if (self.waveName == "sawtooth"):
            for t in range(period):
                if (t < period/2 ):
                    samples[t] = ((2*amplitude)/period)*t
                elif ((t > period/2) and ((((2*amplitude)/period)*t - 2*amplitude) > -32768)):
                    samples[t] = ((2*amplitude)/period)*t - 2*amplitude
                else:
                    samples[t] = -32768
                    
                
        if(DEBUG):
            vis = WaveformVis()
            vis.visSamples(samples, self.waveName)

        return samples

#################################################################
def wait_for_note_start():
    while (True):
        if(DEBUG):
            print "waiting to start"
        
        for key in range(len(keys)):
            if (GPIO.input(keys[key])):
                return key
        sleep(0.1)

def wait_for_note_stop(key):
    while (GPIO.input(key)):
        if(DEBUG):
            print "waiting to stop"
        sleep(0.1)

##################### some initialization ############################################
pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.init()

GPIO.setmode(GPIO.BCM)
keys = [20, 16, 12, 26]
freq = 261.6
waveName = ["square", "triangle", "sinusoidal", "sawtooth"]
notes = []

GPIO.setup(keys, GPIO.IN, GPIO.PUD_DOWN)

for n in range(len(keys)):
    notes.append( Note(freq, 1, waveName[n]))


################## MAin ############################################
print "Welcome to the paper piano"
print "Press Ctrl+C to exit"
try:
    while(True):
        key = wait_for_note_start()
        notes[key].play(-1)
        wait_for_note_stop(keys[key])
        notes[key].stop()
except KeyboardInterrupt:
    print "Bye bye"
    GPIO.cleanup()
    





