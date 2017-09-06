#!/usr/bin/env python

"""
Christine Outlaw
1912737
outla100@mail.chapman.edu
PHYS220
CW 02
"""

# Using a For loop
def coord_for(n,a,b):
    h = float((b-a)/n)
    x =[]
    for i in range(n+1):
        x.append((a+(i*h))
    return x

# Using a While loop
def coord_while(n,a,b):
    h=(b-a)/n
    x=[]
    while a<b:
        x.append(a)
        a = a+h
    return x

# Using a List Comprehension
def coord_comp(n,a,b):
    h=(b-a)/n
    x =[(a+(i*h)) for i in range(n+1)]
    return x

# Main block which takes in user input and calls the 3 previously
# defined functions.
if __name__ == "__main__":
    print("Enter 3 values; n, number of intervals, a, starting point, and b, end point.")
    n,a,b = input("Input in the order and style of n,a,b. ")
    print("Using a for loop: "+coord_for(n,a,b))
    print("Using a while loop: "+coord_while(n,a,b))
    print("Using a list comprehension: "+coord_comp(n,a,b))

