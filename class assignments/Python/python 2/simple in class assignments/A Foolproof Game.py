##############################################################
#Name: Joshua Brack
#Date: 2/3/2019
#Description: Coin toss game, where we see which of three groups wins
########################################################################
from random import randint
#function coin toss
def coinToss():
    toss = randint(0,1)
    if (toss == 0):
        return "Heads"
    elif (toss == 1):
        return "Tails"

#function game
def game(tosses):
    #array storing roundwins
    roundWins = [0,0,0]
    gameWinner = 0
    #simulate coin tosses
    for i in range(tosses):
        coin1 = coinToss()
        coin2 = coinToss()

        if(coin1 == "Heads" and coin2 == "Heads"):
            roundWins[0] = roundWins[0] + 1
        elif (coin1 == "Tails" and coin2 == "Tails"):
            roundWins[1] = roundWins[1] + 1
        else:
            roundWins[2] = roundWins[2] + 1

    #determine winner of round, randomly picking where there is a tie
    if (roundWins[0] > roundWins[1] and roundWins[0] > roundWins[2]):
        gameWinner = 0
    elif (roundWins[1] > roundWins[0] and roundWins[1] > roundWins[2]):
        gameWinner = 1
    elif (roundWins[2] > roundWins[0] and roundWins[2] > roundWins[1]):
        gameWinner = 2
    elif (roundWins[0] == roundWins[1]):
        resolve = randint(0,1)
        gameWinner = resolve
    elif (roundWins[0] == roundWins[2]):
        resolve = randint(0,1)
        if (resolve == 1):
            resolve == 2
        gameWinner = resolve
    elif (roundWins[1] == roundWins[2]):
        resolve = randint(1,2)
        gameWinner = resolve
    elif ((roundWins[0] == roundWins[1]) and (roundWins[0] == roundWins[2])):
        resolve = randint(0,2)
        gameWinner = resolve

    return roundWins, gameWinner

    
####################
#      MAIN PART   #
####################

#declare variables, groupA, groupB, prof, wins
answer = ""
numGames = 0
coinTosses = 0
gameWins = [0,0,0]
gamePercent = [0.0, 0.0, 0.0]
#loop that asks for how many games, then how many coin tosses.
while(True):
    print "\nSay 'exit' or 'bye' with  quotation marks to exit loop\n"
    answer = "" #reset so while will run
    while (not(type(answer) is int or answer == "exit" or answer == "bye")):
        answer = input("How many games? ")
        if (not(type(answer) is int or answer == "exit" or answer == "bye")):
            print "Invalid"

    if (answer == "exit" or answer == "bye"):
        break

    numGames = answer
    answer = "" #reset so while will run
    while (not(type(answer) is int or answer == "exit" or answer == "bye")):
        answer = input("How many coin tosses per game? ")
        if (not(type(answer) is int or answer == "exit" or answer == "bye")):
            print "Invalid"

    if (answer == "exit" or answer == "bye"):
        break

    coinTosses = answer

    #simulate games
    for i in range(numGames):
        #simulate game
        roundRecord, tempWinner = game(coinTosses)
        roundPercent = [0.0, 0.0, 0.0]
        #calculate round percentage
        for j in range(3):
            temp = roundRecord[j]*1.0
            roundPercent[j] = (temp/coinTosses)*100
        print "Game {}".format(i)
        print "\tGroup A: {} ({}%); Group B: {} ({}%); Prof: {} ({}%)".format\
              (roundRecord[0], roundPercent[0], roundRecord[1], roundPercent[1], roundRecord[2], roundPercent[2])
        gameWins[tempWinner] = gameWins[tempWinner] + 1

    #calculate gamepercentage
    for i in range(3):
        temp = gameWins[i]*1.0
        gamePercent[i] = (temp/numGames)*100
        
    print "Wins: Group A={} ({}%); Group B={} ({}%); Prof={} ({}%)".format\
          (gameWins[0], gamePercent[0],gameWins[1], gamePercent[1], gameWins[2], gamePercent[2])

    #reset some variables
    gameWins = [0,0,0]
        
