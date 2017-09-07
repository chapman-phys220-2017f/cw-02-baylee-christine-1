#!/usr/bin/env python

"""
Christine Outlaw
1912737
outla100@mail.chapman.edu
PHYS220-01
CW 02
"""

"""
(b) Show to what value does the sum converges as you let the tolerance become smaller and smaller.
"""

def compute_sum(tol):
    k=1
    con_sum = float(0)
    while tol<1/(k**2):
        con_sum+=(k**2)
        k+=1
    return con_sum

"""
Main block calling the function and showing the value to which the sum converges
"""
if __name__ == '__main__':
    convergence = compute_sum(tol=1e-2)
    print("The sum converges at "+convergence)

    
    
# how do you let tolerance become smaller and smaller?