"""Triangular numbers question"""

try:
    p = int(input("Input p:"))
    q = int(input("Input q:"))

    if p>=q:  #Checking whether p is smaller than q
        print("p must be smaller than q")
    elif p<0:  #Checking whether p and q are positive
        print("p and q must be positive")
    else:
        result = 0  #A running total of the triangular numbers
        t = p
        while t<=q:  #Iterates through the numbers in the range [p,q]
            #The formula for the nth trianglar number is t = n(n+1)/2, and n = ((1+8*t)**0.5-1)/2
            #If t is a triangular number, then n must be an integer
            n = ((1+8*t)**0.5-1)/2  #Finding the value of n for the given value of t
            if n.is_integer():  #Checking whether n is an integer
                result += t
            t += 1

        print(result)
except ValueError:  #If the input values of p and q are non-integers
    print("Inputs must be integers")