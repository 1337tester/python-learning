# -*- coding: utf-8 -*-
"""


"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    result = ()
    for n in range(len(aTup)):
        if n%2 == 0:
            result+=(aTup[n],)
    return result



    