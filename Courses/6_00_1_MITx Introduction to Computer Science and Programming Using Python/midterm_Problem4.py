# -*- coding: utf-8 -*-
"""


"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    assert type(listA) == type(listB) == list, 'Both inputs must be lists'
    assert len(listA) == len(listB), 'The lists must have the same length'
    result = 0
    for i in range(len(listA)):
        assert type(listA[i]) == type(listB[i]) == int, 'All members of lists must be integers'
        result += listA[i]*listB[i]
    return result
    
#print(dotProduct(4,1))