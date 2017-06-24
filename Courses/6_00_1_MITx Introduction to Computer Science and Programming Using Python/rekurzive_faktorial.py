# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:08:11 2016

@author: Miso
"""


def fact(n):
    '''
    prva rekurzivna fcia
    n - integer, returns factorial of it
    '''
    if n ==1:
        return 1
    else:
        return n*fact(n-1)
        
print(fact(6))