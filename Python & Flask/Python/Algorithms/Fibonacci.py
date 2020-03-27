"""
## Simple Fibonacci Program
 
def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)
    """

"""
for n in range (1,101):
    print(n,":",fibonacci(n))

    Now this works, however there will be a point where
    the computer would take more time to process the data
    and as the function is recursive, it will repeat itself
    more than often

    """

""" 
    Introducing Memoization

    The Idea is very simple, store the value in a cache
    of a recent function call so that we dont need to repeat the function
    call for the same value

    """
"""
# Implement Memoization Explicitly

# 1st Create the cache
fibonacci_cache = {}
# 2nd Re-Create the Fibonacci Function
def fibonacci(n):
    # if we habe cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # compute the Nth Term
    if n==1:
        value = 1
    elif n==2:
        value = 1
    elif n>2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    fibonacci_cache[n]=value
    return value

for n in range (1,1001):
    print(n,":",fibonacci(n))
"""

# Lets use python's builtin function to handle the cache
from functools import lru_cache
#lru cache stands for Least Recently Used Cache
@lru_cache() # by default it stores 1020 bytes, it automatically adjusts memory
def fibonacci(n):
    """ Check for valid input """
    if type(n)!=int:
        raise TypeError("Input Must be a Positive int")    
    if n<1:
        raise TypeError("Input Must be a Positive int")
    #Compute the Nth Term
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range (1,50500):
    print(n,":",fibonacci(n))