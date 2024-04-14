import csv
import time
from pynput import keyboard
from CnxReadWriteFunctions import *


# sums up total time taken
#counter = 0
#release_time = time.time()
last = time.time()
log = ""

def on_press(key):
    global log
    global last
    num = (time.time()-last)
    last = time.time()
    num *= 1000
    num = round(num)
    num = str(num)
    num = num.zfill(4)
    log += num
    if key == keyboard.Key.enter:
        return False
    # resets time after keystroke
    

def on_release(key):
    global last
    global log
    # calculate the hold time of the key and add it to the hold_times list
    num = (time.time()-last)
    num *= 1000
    num = round(num)
    num = str(num)
    num = num.zfill(4)
    #commas is for easy conversion to a csv file format, the file that excel reads
    #just rename the results file to .csv in the rename function and itll 
    #open a new excel file with the values in it
    log += num

    if key == keyboard.Key.enter:
        return False

def calculation (username, test_results, editDistance):
    cnx = connect()
    data = read(cnx, username)
    cnx.close()
    base_average = data[0][2]
    base_SD = data[0][3]
    dev_sum = 0
    average_list = [base_average[i:i+4] for i in range(0, len(base_average)-1, 4)]
    test_list = [test_results[i:i+4] for i in range(0, len(test_results)-1, 4)]
    del average_list[0]
    del average_list[0]

    del test_list[0]
    del test_list[0]

    print(base_SD)
    for z in range(len(average_list)):
        try:
            avg = int (average_list[z])
            tst = int (test_list [z])
            deviation = (avg-tst)
            print("avg = ", avg)
            print("test = ", tst)
            print("deviation = ", deviation)
        
            dev_sum += deviation**2
            print("sq of sums = ", dev_sum)
        except:
            if len(test_list) == 0:
                dev_sum = 99999999
            else:
                pass
    
    base_SD = int(base_SD)

    keystrokes_match = False
    print(editDistance)
    print("hello")
    if editDistance == 0 and dev_sum <= base_SD*3:
        keystrokes_match = True

    elif dev_sum <= base_SD*1.1:
        keystrokes_match = True
        print ("Test within acceptable range")

    elif dev_sum > base_SD*3:
        print ("Test outside acceptable range")
        

    return keystrokes_match


