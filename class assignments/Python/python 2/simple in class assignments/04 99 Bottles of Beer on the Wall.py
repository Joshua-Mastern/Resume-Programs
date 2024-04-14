###########################################################################################
# Name: Joshua Brack
# Date: 10/19/2018
# Description: Bottles of beer song accomplished using recursion. Also has correct grammar
###########################################################################################

# the algorithm implemented iteratively
def passSomeBeers(bottles):
        if (bottles > 0):
                # USe plural form of bottles if not 1, else use singular form
                if (bottles != 1):
                        print "{} bottles of beer on the wall.".format(bottles)
                        print "{} bottles of beer.".format(bottles)
                else:
                        print "{} bottle of beer on the wall.".format(bottles)
                        print "{} bottle of beer.".format(bottles)                        

                print "Take one down, pass it around."
                bottles = bottles - 1
                # Use plural form if not 1, else use singular form
                if (bottles != 1):
                        print "{} bottles of beer on the wall.".format(bottles)
                else:
                        print "{} bottle of beer on the wall.".format(bottles)                        
                print
                #call the function inside the function again
                passSomeBeers(bottles)

###############################################
# MAIN PART OF THE PROGRAM
###############################################
passSomeBeers(99)

