###########################################################################################
# Name: Joshua Brack
# Date: 11/6/2018
# Description: Generate a random list given a minimum, maximum, and length of list. Then return statistics on said list.
###########################################################################################
import random
# function that prompts the user for a list size, minimum and maximum values, creates the list, and returns it
def fillList():
    length = input("How many random integers would you like to add to the list? ")
    minimum = input("What would you like the minimum value to be? ")
    maximum = input("What would you like the maximum value to be? ")
    # you must use the list functions discussed in class to add integers to the list
    randList = []
    for i in range(length):
        randList.append(random.randint(minimum, maximum))
    return randList

# function that receives the list as a parameter, and calculates and returns the mean
def mean(varList):
    length = len(varList)
    total = 0.0
    for i in range(length):
        total = total + varList[i]

    return (total/length)      

# function that receives the list as a parameter, and calculates and returns the median
def median(varList):
    varList.sort()
    length = len(varList)
    if (length % 2 == 0): #if number is even
        n1 = (length/2) - 1 #must account for indice starting at 0
        n2 = (length/2) #must account for indice starting at 0
        middle = (varList[n1] + varList[n2])/2.0
    else:
        middlePos = (length/2) #if length number is odd it will take the floor of n/2  and add 1. Since indice starts at 0 don't add 1
        middle = varList[middlePos]
    return middle

# function that receives the list as a parameter, and calculates and returns the range
def rangeNum(varList):
    minimum = min(varList)
    maximum = max(varList)
    return maximum - minimum


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list
nums = fillList()

# display the list
# there is no need to write/call your own function for this part
print "The list: {}".format(nums)

# calculate and display the mean
print "The mean of the list is {}.".format(mean(nums))

# calculate and display the median
print "The median of the list is {}.".format(median(nums))

# calculate and display the range
print "The range of the list is {}.".format(rangeNum(nums))
