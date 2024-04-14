import random

def getNums():
    array = []
    i=0
    while (i < 20):
        x = random.randint(0, 99)
        array.append(x)
        i+=1
    return array
# function returning smallest in an array
def getMin(array):
    smallest = array[0]
    for i in range(1,len(array)):
        if (array[i] < smallest):
            smallest = array[i]
        
    return smallest

# function getting biggest number in array
def getMax(array):
    largest = array[0]
    for i in range(1,len(array)):
        if (array[i] >largest):
            largest = array[i]
        
    return largest

#funtion getting index position of smallest number
def getMinPos (array):
    smallestPos = 0
    for i in range (0, len(array)):
        if (array[i] < array[smallestPos]):
            smallestPos = i
    return smallestPos

#

#################### main program ##########################
nums = getNums()
print nums
print "smallest is {}".format(getMin(nums))
print "largest is {}".format(getMax(nums))
print "index of smallest # {}".format(getMinPos(nums))
