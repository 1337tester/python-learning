# -*- coding: utf-8 -*-
"""


"""
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    assert type(L) == list, 'Input must be a list'
    for i in range(len(L)):
        assert type(L[i]) == list, 'All members of the list must be lists'
        L[i].reverse()
        for n in range(len(L[i])):
            assert type(L[i][n]) == int, 'All members of each sublist must be integers'
    L.reverse()

    
L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L)
print(L)
#print(dotProduct(4,1))