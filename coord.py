#!/usr/bin/env python
                        ### python3

### Should be a comment block
"""
Christine Outlaw
1912737
outla100@mail.chapman.edu
PHYS220
CW 02
"""

### Should only be one docstring like this at top of file, which describes entire module in detail.
"""
3 ways to generate equally spaced coordinates with an interval.
"""

# Using a for loop
def coord_for(n,a,b):
    h=(b-a)/n
    x_for =[]
    for i in range(n+1):
        x_for.append((a+(i*h)))
    return x_for


# Using a while loop
def coord_while(n,a,b):
    h=(b-a)/n
    x_while=[]
    while a<=b:
        x_while.append(a)
        a = a+h
    return x_while



# Using a list Comprehension
def coord_comp(n,a,b):
    h=(b-a)/n
    x_list =[(a+(i*h)) for i in range(n+1)]
    return x_list

### NOTE: This should not be a docstring, but a comment
"""
Main block which takes in user input and calls the 3 previously defined functions.
"""
if __name__ == "__main__":
    print("Enter 3 values; n, number of intervals, a, starting point, and b, end point.")
    n = int(input("Input the number of intervals: "))                                      ### Never use input()
    a = float(input("Input a start point: "))
    b = float(input("Input the end point: "))
    print("For loop: " + str(coord_for(n,a,b)))
    print("While loop: " + str(coord_while(n,a,b)))
    print("List comprehension: " + str(coord_comp(n,a,b)))

