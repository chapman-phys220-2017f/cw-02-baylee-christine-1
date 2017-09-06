#!/usr/bin/env python

"""
Christine Outlaw
1912737
outla100@mail.chapman.edu
PHYS220
CW 02
"""

# Using a For loop
def coord_for(n, a, b):
    h = float((b-a)/n)
    x =[]
    for i in range(n+1):
        x.append(a)
        a = a+h
    return x
coord_for(9,0,1)


# Using a While loop
def coord_while(n, a, b):
    h=(b-a)/n
    x=[]
    while a<b:
        x.append(a)
        a = a+h
    return x
coord_while(9,0,1)



# Using a List Comprehension
def coord_comp(n, a, b):
    h=(b-a)/n
    x =[(a+(i*h)) for i in range(n+1)]
    return x
coord_comp(9,0,1)