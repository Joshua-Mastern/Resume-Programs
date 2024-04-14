#######################################################################################################################################################################
# Name: Joshua Brack                                                                                                                                                  #
# Date: 9/28/2018                                                                                                                                                     #
# Description: take test score and return letter grade                                                                                                                #
#######################################################################################################################################################################
name = input("what is your name?: ")
score = input("Hey {}, what did you get on the test? ".format(name))

if(score >= 90):
    print "You got an A"
elif (score >= 80):
    print "You got an B"
elif (score >= 70):
    print "You got an C"
elif (score >= 60):
    print "You got a D"
else:
    print "You have failed..."
