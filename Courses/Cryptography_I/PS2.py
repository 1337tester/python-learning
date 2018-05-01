import itertools

def encrypt(k, x):
    t = k[0]
    result = ''
    for i in [1,2,3,4]:
        if int(x[i-1]) == 1:
            t = t ^ k[i]
        result += str(t)
    return result

# lst = list(itertools.product([0, 1], repeat=5))
# sett = [['0110', '0011'], ['0101', '1010'], ['1110', '0110']]
# m = '0101'
# c = '1010'
# for k in lst:
#         # if encrypt(k, m) == c:
#         print ':'.join(['for key', str(k), ' the result is', encrypt(k, m)])





# 101011000001111010101100101011000001111010101000101000001010100
# 100010101001011100010101000101000000100010100