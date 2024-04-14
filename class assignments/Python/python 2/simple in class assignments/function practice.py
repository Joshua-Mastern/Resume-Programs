###########################################################################################
#Name: Joshua Brack
#Date: 10/1/2018
#Description: Function practice
############################################################################################
def func1(first, second): #function that takes two arguments and raises the first argument by the power of the second argument
    return first**second

def bigBoy(first, second): # function that takes two arguments and returns the larger argument
    if (first > second):
        return first
    elif (second > first):
        return second

def littleBear ( first, second): # finds smaller value of two arguments
    if (first < second):
        return first
    else:
        return second

def printer(a):         #prints out argument
    print "The answer is {}".format(a)


############################### use functions

firstNumber = input("Give me a number ")
secondNumber = input("Give me another number ")

#calculate small number raised to the power of the larger number
z = func1( littleBear(firstNumber, secondNumber), bigBoy(firstNumber, secondNumber))
printer(z)
