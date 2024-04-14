import csv
import time
from pynput import keyboard
from hashingFunction import *


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
    log += num ##+ ","
    if key == keyboard.Key.enter:
        return False
    

def on_release(key):
    global last
    global log
    # calculate the hold time of the key and add it to the hold_times list
    num = (time.time()-last)
    num *= 1000
    num = round(num)
    num = str(num)
    num = num.zfill(4)
   
    log += num 

    if key == keyboard.Key.enter:
        return False

def average (totals, attempts):
    # takes the list of the totals of the data points and divides them by the number of attempts to calculate the averages
    for i in range(len(totals)):
        totals[i] = totals[i]/attempts
    
    # stores the averages in one concatenated number
    average_number = "".join(str(int(i)).zfill(4) for i in totals)

    return average_number, totals



def standard_dev(average_list, keystroke_list, attempts):
    sum = 0
    counter1 = 0
    counter2 = 4
    for i in range(len(average_list)):
        SD = 0
        j = 0
        if j < len(keystroke_list):
            try:
                z = ((int(keystroke_list[j][counter1:counter2])-int(average_list[i]))**2)
                SD += z

            except:
                pass
            
            #outlier handling
            if int(SD/float(average_list[i])) > 0.5:
                navg = 0 
                ksd = keystroke_list
                avg = average_list[i]
                sd = SD
                for i in range(len(ksd)):
                    if int(ksd[i][counter1:counter2]) > float(avg) + float(sd) or int(ksd[i][counter1:counter2]) < float(avg) - float(sd):
                        txt = ksd[i]
                        txt = txt.replace(ksd[i][counter1:counter2],"0000")
                        ksd[i]= txt
        
            else:
                navg += int(ksd[i][counter1:counter2])
            
            average_list[i]= str(navg/i)
            keystroke_list = ksd

        counter1 += 4
        counter2 += 4   
        sum += SD/attempts
        j+=1

    return sum

def create_user(user, password1, password2):
        global log
        global last
        user_create = user
        pass_create = password1
        pass_confirm = password2



        
        if pass_create == pass_confirm:
            attempts_needed = 20
            attempts = 0
            list_of_results = []
            while attempts < attempts_needed:
                log = ""
                last = time.time()
                with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
                    listener.join()

                with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
                    last = time.time()
                    listener.join()
                
                # creates a list that will add up the total time for each keystroke data point
                if attempts == 0:
                    totals = [int(log[i:i+4]) for i in range(0, len(log)-1, 4)]
                
                # adds the new data to the totals list
                else:
                    for i in range(len(totals)):
                        try:
                            trial = [int(log[i:i+4]) for i in range(0, len(log)-1, 4)]
                            totals[i] += trial[i]
                        except:
                            pass

                list_of_results.append(log)
                
                

                #increments the number of attempts
                attempts += 1
                #informs the user of how many attempts are left
                
                
                if attempts == attempts_needed:
                    # calculates and stores the averages for the keystroke data points1
                    average_num, average_list = average(totals, attempts)

                    standard_deviation = int(standard_dev(average_list, list_of_results, attempts))

                                        
                    newpassword(user_create, pass_create, average_num, standard_deviation)
                    
         
                        
                    break
                last = time.time()

