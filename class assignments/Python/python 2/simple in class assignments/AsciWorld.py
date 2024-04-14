#draw asci person
from time import sleep
from os import system
import keyboard

ROW = 20
COL = 20
def drawPerson():
    #       O         
    #     --|--      
    #       |        
    #      | |
    arr = [[' ',' ','O',' ',' '],
           ['-','-','|','-','-'],
           [' ',' ','|',' ',' '],
           [' ','|',' ','|',' ']]
    return arr

def drawWorld(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print arr[i][j],
        print

def submit(parent, child, c, r):
    #takes a child array and posts it into parent array
    for i in range(len(child)):
        for j in range(len(child[i])):
            parent[c+i][r+j] = child[i][j]

#def fillArr(arr, r, c):
#    for row in range(r):
#        arr.append([])
#    for col in range(c):
#        if ((row == 0 or row == r-1) and col > 0 and col < c-1):
#            arr[row].append('_')
#        elif((col == 0 and row >0) or (col == c-1 and row >0)):
#            arr[row].append('|')
#        else:
#            arr[row].append('*')
    
####MAIN###
#world is what all information to be drawn will be placed in, x, y
running = True
world = []
#fill in stuff for list world
for row in range(ROW):
    world.append([])
    for col in range(COL):
        if ((row == 0 or row == ROW-1) and col > 0 and col < COL-1):
            world[row].append('_')
        elif((col == 0 and row >0) or (col == COL-1 and row >0)):
            world[row].append('|')
        else:
            world[row].append(' ')
#fillArr(world, ROW, COL)
#add person to world

#player row, this variable is incremented to move person on board
pr = 0
#player column, this variable is incremented to move person on board
pc = 0
while(running):
    submit(world, drawPerson(), 3+pc, 5+pr)
    drawWorld(world)
    #add movement using wasd
    if (keyboard.is_pressed('d')):
        pr += 1
    elif (keyboard.is_pressed('a')):
        pr -= 1
    elif (keyboard.is_pressed('w')):
        pc -= 1
    elif (keyboard.is_pressed('s')):
        pc += 1
    

    system("cls")
    #exit game if pressed
    if (keyboard.is_pressed('esc')):
        running = False
    
        
