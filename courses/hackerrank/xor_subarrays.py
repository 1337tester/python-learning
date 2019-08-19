
def sansaXor(arr):
    """ XORs of the result of subsequent XORing all the sublists """
    result = 0
    xors = []
    for sublist in sub_lists(arr):
        subresult = 0
        # print(sublist)
        for number in sublist:
            subresult = subresult ^ number
        xors.append(subresult)
    # print(xors)
    for number in xors:
        result = result ^ number
    return result

def sub_lists(list1):
    """ Creating all the sublists from a list """
    sublists = []
    for i in range(0, len(list1) + 1):
        for j in range(i + 1, len(list1) + 1):
            sub = list1[i:j]
            sublists.append(sub)
    return sublists

print(sansaXor([3, 4, 5]))
