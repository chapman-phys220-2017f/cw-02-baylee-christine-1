#!/usr/bin/env python
                                       ### Don't forget to specify python3

### NOTE the following should be a block comment, not a docstring. You should also have a docstring that describes what is in the module, but this block comment is only for Chapman coding standards.
'''
Baylee Mumma
mumma103@mail.chapman.edu
PHYS220-01
CW 02
'''

def fibs(n):
    fl = [1,1]
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        for i in range(2,n):
            fl.append(fl[i-2]+fl[i-1])
            return fl
    
def fib_generator():
    a = 1
    b = 1
    while True:
        yield a
        a,b = b,a+b

### NOTE : the following should be in a main block
g = fib_generator()
fl = [next(g) for _ in range(5)]
print(fl) 


