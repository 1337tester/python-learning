# -*- coding: utf-8 -*-
"""


"""

def dict_interdiff(d1, d2):
    intersect = {}
    difference = {}
    for a in d1.keys():
        if a in d2.keys():
            intersect[a] = f(d1[a], d2[a])
        else:
            difference[a] = d1[a]
    for b in d2.keys():
        if b not in d1.keys():
            difference[b] = d2[b]
    result = (intersect, difference)
    print(result)
    return result

def f(a, b):
    return a+b


d1 = {1:1, 4:2, 6:3, 2:5}
d2 = {1:3, 2:6, 3:9, 200:1, 12:12}
dict_interdiff(d1, d2)
#print(dotProduct(4,1))