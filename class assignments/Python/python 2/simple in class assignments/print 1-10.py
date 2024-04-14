#################
#
#
####################
#function print song 99 bottle of beer
def beerOnWall(beer):
    #repeat song till 0 bottles of beer are on the wall
    while(beer > 0):
        print "{} bottles of beer on the wall, {} bottles of beer on the wall\
                \ntake one down pass it around, ".format(beer, beer)
        if (beer < 2):
            print "{} bottle of beer on the wall".format(beer)
        else:
            print "{} bottles of beer on the wall".format(beer)
        print "_" *40
        beer -=1


########################
#main part pf program
########################
beerOnWall(99)
