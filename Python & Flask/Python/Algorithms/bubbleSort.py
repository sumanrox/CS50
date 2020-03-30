# Bubble sort using Recursion Technique

def bubble_sort(listt): 
    for i, num in enumerate(listt): 
        try: 
            if listt[i+1] < num:       # if the current item is greater than next item
                listt[i] = listt[i+1]  # swap now
                listt[i+1] = num 
                bubble_sort(listt) # call itself again
        except IndexError: # if any problem with indexing, like idexOutOfBound, handle the error
            pass
    return listt 

listt = [64, 34, 25, 12, 22, 11, 90] 
bubble_sort(listt) 
  
print("Sorted array:"); 
for i in range(0, len(listt)): 
    print(listt[i]), 
