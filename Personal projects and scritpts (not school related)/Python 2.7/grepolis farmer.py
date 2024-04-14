##################################
#Grepolis farmer
####################################

import keyboard
import mouse
import time

#testing mouse stuff
#events = mouse.record()
#mouse.play(events)


#get what you want
print "Hello, when you are ready to begin recording hit enter. To stop recording hit the right mouse button."
keyboard.wait(hotkey= "enter")

events = mouse.record()

#time until next execution
val = input("Enter number of minutes you want to wait ")

#convert to seconds
val = val * 60
print "you chose {} seconds".format(val)

try:
        i = 1
        while (True):
                print
                print "waiting"
                time.sleep(val)

                print "rotation {}... begin".format(i)
                mouse.play(events)
                print
                print "done with that rotation"
                i= i+1

except KeyboardInterrupt:
        print "Thanks and come again"
