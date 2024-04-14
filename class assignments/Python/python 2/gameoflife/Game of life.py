import sys
from copy import deepcopy
from time import sleep
from os import system

NUMGENS = 10
SLEEPTIME = 0.5

def printBoard(arr, gen):
    print "Gen {}".format(gen)
    
    print " ",
    for col in range(1, size-1):
        print col%10,
    print
    for row in range(1, size-1):
        print row%10,
        for col in range(1, size-1):
            print arr[row][col],
        print
        
def computeNextGen(board):
    nextBoard = deepcopy(board)
    for row in range(1, size-1):
        for col in range(1, size-1):
            neighbours = countNeighbours(board, row, col)
            if (board[row][col] == "*"): # cell is alive
                if(neighbours < 2 or neighbours > 3):
                    nextBoard[row][col] = " " # it DIES
            else:
                if (neighbours == 3):
                    nextBoard[row][col] = "*" #it becomes alive

    return nextBoard


def countNeighbours(board, row, col):
    neighbours = 0
    for i in range(-1, 2):
        for j in range (-1, 2):
            if (not(i == 0 and j == 0)):
                if (board[row+i][col+j] == "*"):
                    neighbours += 1
    return neighbours

board = []

for line in sys.stdin:
    size = len(line) - 1
    board.append([])
    for i in range(size):
        board[len(board) - 1].append(line[i])
try:
    for i in range(NUMGENS):
        printBoard(board, i)
        board =  computeNextGen(board)
        sleep(SLEEPTIME)
        system("cls")

except KeyboardInterrupt:
    printboard(board, "last")
    print "Bye bye"
