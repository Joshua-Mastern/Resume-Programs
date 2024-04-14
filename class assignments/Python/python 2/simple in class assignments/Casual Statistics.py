###########################################################################################
# Name: Joshua Brack 
# Date: October 9, 2018
# Description: Take three inputs and return math statistics on them.
###########################################################################################

# function that prompts the user to enter an integer and returns it
def give():
    number = input ("Enter an integer: ")
    return number

# function that receives three integers as parameters and returns the minimum of the three
def minimum(num1, num2, num3):
    if(num1 <= num2 and num1 <= num3):
        return num1
    elif(num2 <= num1 and num2 <= num3):
        return num2
    elif(num3 <= num1 and num3 <= num2):
        return num3

# function that receives three integers as parameters and returns the maximum of the three
def maximum(num1, num2, num3):
    if (num1 >= num2 and num1 >= num3):
        return num1
    elif (num2 >= num1 and num2 >= num3):
        return num2
    elif (num3 >= num1 and num3 >= num2):
        return num3

# function that receives three integers as parameters, and calculates and returns the mean
def mean (num1, num2, num3):
    avg = (num1+num2+num3)/3.0
    return avg

# function that receives three integers as parameters, and calculates and returns the median
def median (num1, num2, num3):
    first = minimum(num1, num2, num3)
    third = maximum(num1, num2, num3)
    #figure out if a number repeats
    repeated = mode(num1, num2, num3)
    if ( num1 > first and num1 < third):
        return num1
    elif (num2 > first and num2 < third):
        return num2
    elif (num3 > first and num3 < third):
        return num3
    elif (repeated != "undefined"):
        return repeated             #if a number repeats it is guaranteed to be the median in a list of 3 numbers

# function that receives three integers as parameters, and calculates and returns the mode
def mode (num1, num2, num3):
    if (num1 == num2 or num1 == num3):
        return num1
    elif (num2 == num3):
        return num2
    else:
        return "undefined"
    

# function that receives three integers as parameters, and calculates and returns the range
def range_ (num1, num2, num3):
    low = minimum(num1, num2, num3)
    high = maximum(num1, num2, num3)
    return high - low


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# get three integers from the user
num1 = give() #1 integer
num2 = give() #2 integer
num3 = give() #3 integer

# determine and display the minimum value
print "The minimum value is {}.".format(minimum(num1, num2, num3))

# determine and display the maximum value
print "The maximum value is {}.".format(maximum(num1, num2, num3))

# calculate and display the mean
print "The mean is {}.".format(mean(num1, num2, num3))

# calculate and display the median
print "The median is {}.".format(median(num1, num2, num3))

# calculate and display the mode
print "The mode is {}.".format(mode(num1, num2, num3))

# calculate and display the range
print "The range is {}.".format(range_(num1, num2, num3))

