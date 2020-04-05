# set an array of 6 items
array=[1,45,67,2,7,18]
item = 2
#then search for the item
def search(array,item):
    for i in range(len(array)):
            if array[i]==item:
                            print("[*] Found ",item)
    return -1