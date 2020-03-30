# Recursive method for Selection Sort

"""
Now lets create a function that can provide
us with minimum value for the current index

"""
def minIndex(array,index,otherElement):
    if index==otherElement:
        return index
    k=minIndex(array,index+1,otherElement)
    return(index if array[index]<array[k] else k)

"""
Now lets create a recursive function to do a selection sort
n is size of array[] and index is the index of starting element
"""

def selectionSort(array,n,index=0): # we are providing a default value for index
    # Return when starting and size are same
    if index == n:
        return -1
    # calling minimm index function
    # for minimum index
    k=minIndex(array,index,n-1)


    # now if there is a chance that we have got a smaller
    # element in the array than the one which we currently
    # have on the index
    # we can swap their position
    if k != index: 
        array[k], array[index] = array[index], array[k] 
    
    # Recursively calling selection sort function
    selectionSort(array,n,index+1)

# Lets now create the driver code
array=[25,6,1,0,99,1,23,12,3,6,445]
n=len(array)

# Calling the function
selectionSort(array,n)

# printing sorted array
print("\n[*] Sorted Elements")
for i in array:
    print(i,end=' ')
print("\n")
