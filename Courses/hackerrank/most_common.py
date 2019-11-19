"""
You are given a string  which contains only lowercase English characters.
Your task is to find the top three most common characters in the string .

Input Format
A single line of input containing the string .

Output Format
Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in ascending order.

Sample Input
aabbbccde

Sample Output
b 3
a 2
c 2
"""

# failing on 'qwertyuiopasdfghjklzxcvbnm' ->
# a 1
# b 1
# c 1


#!/bin/python3
from collections import OrderedDict, Counter

if __name__ == "__main__":
    # s = input().strip()
    s = 'abcdefghijjjklmno'.strip()
    dicti = {}
    for a in s:
        if a in dicti: dicti[a] += 1
        else: dicti[a] = 1

dicta = OrderedDict(sorted(OrderedDict(sorted(dicti.items(), key=lambda t: t[0], reverse=True)).items(), key=lambda t: t[1]))

for i in range(3):
    a,b = dicta.popitem()
    print(a, b)


#elegant solution from other guy
'''
class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted('abcdefghijjjklmno')).most_common(3)]
'''