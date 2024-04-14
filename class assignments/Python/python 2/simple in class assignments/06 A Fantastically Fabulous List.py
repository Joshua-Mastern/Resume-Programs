###########################################################################################
# Name: Joshua Brack
# Date: 11/1/2018
# Description: A program that asks the user to provide information for a list.
###########################################################################################

# function that:
def fillList():
    array = []
    # (1) prompts the user for a list size
    listSize = input("How many integers would you like to add to the list? ")
    # (2) prompts the user for the integers to store in the list (corresponding to the list size)
    for i in range (listSize):
        # (3) creates the list
        temp = input("Enter an integer: ")
        array.append(temp)
    # (4) returns the list
    return array



###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list
nums = fillList()

# display information about the list using the list functions discussed in class
# there is no need to write/call your own functions here

print "The original list is: {}".format(nums)
print "The length of the list is: {}.".format(len(nums))
print "The minimum value in the list is: {}.".format(min(nums))
print "The maximum value in the list is: {}.".format(max(nums))
nums.reverse()
print "The reversed list: {}".format(nums)
nums.sort()
print "The sorted list: {}".format(nums)
