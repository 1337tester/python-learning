# -*- coding: utf-8 -*-
"""


"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    M = L[:]
    for i in M:
        if not g(f(i)):
            L.remove(i)
    if L == []:
        return -1
    return max(L)
            

def f(i):
    return i + 2
def g(i):
    return i > 5


L = [1, 2, 63, 25]
print(applyF_filterG(L, f, g))
print(L)