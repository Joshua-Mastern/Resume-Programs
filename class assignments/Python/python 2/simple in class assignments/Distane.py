##################################################################################
# Name: Joshua Brack
# Date: 10/21/2018
# Description: Find distance between two points
####################################################################################

#Get input


#Distance function
def distance (x1, y1):
    stepOne = x1**2 +y1**2
    stepTwo = stepOne**.5
    return stepTwo


################################################################################
# Main part of program.
#################################################################################
#looop forever
while (True):
    x1 = input("provide the x for point 1 ")
    y1 = input("provide the y for point 1 ")
    answer = distance(x1,y1)
    print answer
