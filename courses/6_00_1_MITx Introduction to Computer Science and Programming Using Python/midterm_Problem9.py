# -*- coding: utf-8 -*-
"""


"""

#result = []
#def flatten(aList):
#    ''' 
#    aList: a list 
#    Returns a copy of aList, which is a flattened version of aList 
#    '''
#    for a in aList:
#        if type(a) == list:
#            result.append(flatten(a))
#        else:
#            result.append(a)
#    return result
def flatten(aList, result = []):
    for a in aList:
            if type(a) == list:
                flatten(a)
            else:
                result.append(a)
    return result
    

#def flatten(aList):
#    ''' 
#    aList: a list 
#    Returns a copy of aList, which is a flattened version of aList 
#    '''
#    def flatten_helper(lista, result = []):
#        for a in lista:
#            if type(a) == list:
#                flatten_helper(a)
#            else:
#                result.append(a)
#        return result
#    result = flatten_helper(aList)
#    return result


L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
#L = [[1], [2, 3]]
print(flatten(L))