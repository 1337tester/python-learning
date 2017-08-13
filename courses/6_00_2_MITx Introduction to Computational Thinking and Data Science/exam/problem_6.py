# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 17:22:02 2016

@author: Miso
"""

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    import numpy as np
    import itertools    
    result = np.zeros((len(choices),), dtype=np.int)
    cmb = []
    for x in range(1, len(choices) + 1):
        cmb += itertools.combinations(choices, x)
    valid_combos = [i for i in cmb if sum(i) == total]
    if valid_combos == []:
        less_combos = [i for i in cmb if sum(i) <= total]
        right_combo = []
        for i in less_combos:
            if sum(i) > sum(right_combo):
                right_combo = i
    else:
        right_combo = valid_combos[0]
        for i in valid_combos:
            if len(i) < len(right_combo):
                right_combo = i
    right_list = list(right_combo)
    for i in range(0, len(choices)):
        if choices[i] in right_list:            
            result[i] = 1
            right_list.remove(choices[i])
    return result     
    

print(find_combination([2,5,6,9,9,6,3,1,4,5], 8))
print(find_combination([10, 10, 11, 11, 11], 20))
print(find_combination([3, 10, 2, 1, 5], 12))