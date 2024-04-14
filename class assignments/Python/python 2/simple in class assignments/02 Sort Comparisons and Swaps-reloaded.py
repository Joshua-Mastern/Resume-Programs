######################################################################################################################
# Name: Joshua Brack
# Date: 12/10/2018
# Description: Sort a list with each type of sort and plot number of comparisons and swaps. Assumed there is a module name plot to import from.
######################################################################################################################
from plot import plot

# creates the list
def getList():
#       return [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]
       return [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]
#       return [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]
#       return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#       return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#       return [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]

# the bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def bubbleSort(items):
        comps = 0
        swaps = 0
        n = len(items)
        for i in range (1,n):
                for j in range(1, n-i +1):
                        comps += 1
                        if (items[j] < items[j-1]):
                                swaps += 1
                                temp = items[j]
                                items[j] = items[j-1]
                                items[j-1] = temp
        return comps,swaps

                
        


# the optimized bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def optiBubbleSort(items):
        comps = 0
        swaps = 0
        n = len(items)
        for i in range (1,n):
                isSwapped = False
                for j in range(1, n-i +1):
                        comps += 1
                        if (items[j] < items[j-1]):
                                isSwapped = True
                                swaps += 1
                                temp = items[j]
                                items[j] = items[j-1]
                                items[j-1] = temp
                if(isSwapped == False):
                        break
        return comps,swaps


# the selection sort function
# input: a list of integers
# output: a number of comparisons and swaps
def selectionSort(items):
        comps = 0
        swaps = 0
        n = len(items)
        for i in range(n-1):
        #find smallest number and swap it with the current position
                minPosition = i
                for j in range(i+1, n):
                        comps += 1
                        if (items[j] < items[minPosition]):
                                minPosition = j
                #performing swap
                swaps += 1
                temp = items[i]
                items[i] = items[minPosition]
                items[minPosition] = temp
        return comps,swaps


# the insertion sort function
# input: a list of integers
# output: a number of comparisons and swaps
def insertionSort(items):
        comps = 0
        swaps = 0
        n = len(items)
        for i in range(1, n):
                comps+=1
                if(items[i-1] > items[i]):
                        
                        temp = items[i]
                        j = i - 1
                        while (j >= 0 and items[j] > temp):
                                comps+=1
                                swaps+=1
                                items[j+1] = items[j]
                                j-=1
                        comps+=1
                        items [j+1] = temp
                     
        return comps,swaps
                
                

                

                
                

# the main part of the program

#bubble sort
nums = getList()
print "The list: {}".format(nums)
comparisons, swaps = bubbleSort(nums)
print "After bubble sort: {}".format(nums)
print "{} comparisons; {} swaps".format(comparisons, swaps)
print ""
bubble = [comparisons, swaps]

#optimized bubble sort
nums = getList()
print "The list: {}".format(nums)
comparisons, swaps = optiBubbleSort(nums)
print "After optimized bubble sort: {}".format(nums)
print "{} comparisons; {} swaps".format(comparisons, swaps)
print ""
optimized = [comparisons, swaps]

#Selection sort
nums = getList()
print "The list: {}".format(nums)
comparisons, swaps = selectionSort(nums)
print "After selection sort: {}".format(nums)
print "{} comparisons; {} swaps".format(comparisons, swaps)
print ""
selection = [comparisons, swaps]

#Insertion sort
nums = getList()
print "The list: {}".format(nums)
comparisons, swaps = insertionSort(nums)
print "After insertion sort: {}".format(nums)
print "{} comparisons; {} swaps".format(comparisons, swaps)
print ""
insertion = [comparisons, swaps]

plot(bubble, optimized, selection, insertion)
