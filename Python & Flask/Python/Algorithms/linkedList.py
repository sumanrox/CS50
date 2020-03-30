# A Python implementation of linked list

# First lets create a Node
class Node:

    # Function to initialise the node object
    def __init__(self,name,phone):
        self.name=name # Assign the node data
        self.phone=phone 
        self.next=None # Pointer to none

# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head=None

    # Lets print the data in the Linked List
    # starting from the head
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.name,temp.phone)
            temp=temp.next

# Code execution starts here
if __name__ == "__main__":
    # Start with empty list
    myList=LinkedList()
    # Lets give them some data
    myList.head=Node("Suman Roy",'556-268-1999')
    second=Node("Anne Hilton",'258-123-1893')
    third=Node("Travis Mcaffee",'768-989-1209')

    """
    Now the data has been assigned but they are not linked
    to each other's addresses
    """
    myList.head.next=second
    second.next=third
    third.next=None

    print("\n[*] Accessing the Linked List : \n")
    myList.printList()
