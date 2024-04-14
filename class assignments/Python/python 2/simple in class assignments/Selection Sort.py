#############################################
#
#
#Description: Selection Sort

def selectionSort(array):
    n = len(array)
    for i in range(n-1):
    #find smallest number and swap it with the current position
        for j in range(i+1, n):
            if (array[j] < array[i]):
                #performing swap
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
            print array
    print array

#########    Main Part #######
nums =  [5, 4, 3, 2, 9,7, 13,6]
selectionSort(nums)
print nums
