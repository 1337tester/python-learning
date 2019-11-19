# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 16:03:03 2016

@author: Miso
"""

def fib(x):
    '''
    assume x is an integer >= 0
    returns fibonacci of x
    '''
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        
def genFib():
    fib_1 = 1
    fib_2 = 2
    while True:
        next = fib_1 + fib_2
        yield next
        fib_1 = fib_2
        fib_2 = next

a = genFib()





    