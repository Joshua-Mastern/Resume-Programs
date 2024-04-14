##########################################################################################
# Name: Joshua Brack
# Date: 10/27/2018
# Description: Generate a table comparing binary search to sequential search,
#               based on user-given min, max, and interval.
##########################################################################################
import math
# a function that displays the table
def table (minimum, maximum, interval):
    ranger = maximum - minimum
    print "n       Seq     Bin     Perf"
    print "-"*32
    #begin loop of 4 loops
    number = minimum
    while (number <= maximum):
        sequential = avgSeq(number)
        binary = maxBin(number)
        
        if (binary != 0):# protect against dividing by 0
            performance = (float(sequential))/binary
        else:
            performance = 0
        performance = round(performance)
        print "{:<8}{:<8}{:<8}{:<8}".format(number, sequential, binary, math.trunc(performance))
        number += interval
    
    

# a function that calculates the average number of comparisons of a sequential search on a list of size n
def avgSeq (n):
# -input: the list size
# -output: the average number of comparisons
    return n/2


# a function that calculates the maximum number of comparisons of a binary search on a list of size n
def maxBin(n):
# -input: the list size
# -output: the average number of comparisons
    x = math.log(n+1, 2)
    x = math.ceil(x)
    return math.trunc(x)


###############################################
# MAIN PART OF THE PROGRAM
###############################################
# get user input for the minimum (make sure that it is >= 0)
minValue = -1
while (minValue < 0):
    minValue = input("Minimum number of list items (>=0)? ")
    if (minValue < 0):
        print " *ERROR: Minimum must be >= 0!"

# get user input for the maximum (make sure that it is >= minimum)
maxValue = -1
while (maxValue < minValue):
    maxValue = input("Maximum number of list items (>= min ({}))? ".format(minValue))
    if (maxValue < minValue):
        print " *ERROR: Maximum must be >= minimum ({})!".format(minValue)

# get user input for the interval (make sure that it is >= 1)
interval = -1
while (interval < 1):
    interval = input("The interval between each row of the table (>= 1)? ")
    if (interval < 1):
        print " *ERROR: Interval must be >= 1!"

# generate the table
table(minValue, maxValue, interval)

