#!/usr/bin/env python

"""
Christine Outlaw
1912737
outla100@mail.chapman.edu
PHYS220-01
CW 02
"""

"""
Function to compute the infinite sum.
"""

def compute_sum(tol):
    k=1
    con_sum = 0
    next_term = 1/(k**2)
    while tol<next_term:
        next_term = 1/(k**2)
        con_sum+=next_term
        k+=1
    return con_sum

"""
Main block calling the function and showing the value to which the sum converges to as tolerance gets smaller
"""
if __name__ == '__main__':
    convergence = compute_sum(tol=1e-2)
    print("The sum converges at "+convergence+" when tolerance is set to 1e-2")
    small_tol_convergence = compute_sum(tol=1e-10)
    print("The sum converges at "+small_tol_convergence+" when tolerance is set to 1e-10. This can be rounded to 1.645")