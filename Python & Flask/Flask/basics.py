def typeCast(): #Type Casting example
    x=int(input("Enter a Number : ")) #converting the user input to integer
    if x > 0:
        print("x is positive")
    elif x<0:
        print("x is negative")
    else:
        print("x is zero")

typeCast() #calling the function

name="Josh" #string
names=["Krishna","Julia","Athena"] #list
tupple=(2,8,5) #tupple, immutable data structures

#for loop
for name in names: #call each item in the list as name
    print(f"Hello, {name}") #and then print it, as a formatted strings

#range function
for i in range(10):
    print(i)

#set
s= set()
s.add(5)
s.add(10)
s.add(56)
s.add(39)
#is 28 in the set?
print(28 in s)#returns boolean

#dictionaries
ages={
    "Alice":28,
    "Bob":25,
    "David":65
}
#increment the value of a key
ages["Bob"] +=1
print(ages)

#remove a key from the dictionary
del ages["David"]
print(ages)

#Adding a key in the dictionary
ages["Sven"]=23
print(ages)