############################SORT GODS#####################################
#Name: Joshua
#Date: 11/30/2018
#Descripton: A calling upon the great gods of sorting to allow us to use their great abilities
###########################################################################

#BUBBLE god
def bigGBubble(items):
    n = len(items)
    for i in range (1,n):
        for j in range(1, n-i +1):
            if (grades[j] < items[j-1]):
                temp = items[j]
                items[j] = items[j-1]
                items[j-1] = temp
#INSERTION god
def bigGInsert(items):
    i = 1
    n = len(items)
    while (i < n):
        if (list[i-1] > list[i]):
            temp = list[i]
            j=i-1
            while (j >= 0 and list[j] > temp):
                list[j+1] = list[j]
                j-= 1
                list[j+1] = temp
            i += 1

######ACTIVATION###########
#     BE PREPARED         #
#                         #
###########################
list = [2, 81, 63, 4, 96]



