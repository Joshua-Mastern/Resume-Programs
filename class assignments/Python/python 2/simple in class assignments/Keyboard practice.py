import keyboard
c = input("enter a character")
while(True):
    
    if(keyboard.is_pressed(c)):
        print "pressed {}".format(c)
