###########################################################################################
# Name: Joshua Brack    
# Date: 9/28/2018
# Description: Ask a user for name and age. Return name and age in a creative way.
###########################################################################################

# prompt the user for a name and an age
name = input("Please enter your name: ") # will print question and wait for input

age = input ("How old are you, " + name + "? ") # will print question using name and wait for input

# display the final output
print ("Hi, " + name + ". You are " + str(age) + " years old. Twice your age is " + str(age*2) + ".") 



