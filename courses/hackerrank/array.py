import numpy
def arrays(arr):
    return numpy.array(arr, float)[::-1]

arr = '1 2 3 4 -8 -10'.strip().split(' ')
result = arrays(arr)
print(result)
