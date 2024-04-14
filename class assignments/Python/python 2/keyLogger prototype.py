import time
from pynput import keyboard

#list of times between keys
times = []

#list of key hold times
hold_times = []

log = ""

#sums up total time taken
counter = 0
start_time = time.time()


def on_press(key):
    global log
    global last
    global counter
    global times
    global start_time
    try:
        log = log + "[" + str(time.time()-last) + "] " + key.char + "\n"
    except AttributeError:
        if key == key.space:
            log = log + "[" + str(time.time()-last) + "] SPACE\n"
        else:
            log = log + "[" + str(time.time()-last) + "] " + str(key) + "\n"
    
    #add to total time counter
    counter+= time.time()-last

    #append time between keys to the list
    times.append(time.time()-last)

    #resets time after keystroke
    last = time.time()

    #start tracking hold time
    start_time = time.time()

def on_release(key):
    global hold_times
    global start_time
    global log

    #calculate the hold time of the key and add it to the hold_times list
    hold_time = time.time() - start_time
    hold_times.append(hold_time)

    #add the hold time to the log
    log = log + "[Hold time: " + str(hold_time) + "]\n"

    if key == keyboard.Key.esc:
        return False
   

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    last = time.time()
    listener.join()

#calculates the average time between key presses
between_avg = sum(times)/len(times)

#calculates the average hold time of a key
hold_avg = sum(hold_times)/len(hold_times)

with open("results.txt", "a") as f:
    f.write(log)
    f.write("Total time: " + str(counter) + " seconds\n")
    f.write("Average time between key presses: " + str(between_avg) + " seconds\n")
    f.write("Average hold time of a key: " + str(hold_avg) + " seconds\n")
    f.write("\n")

print("The log has been written to results.txt")
