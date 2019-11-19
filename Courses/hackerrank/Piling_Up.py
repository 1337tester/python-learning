"""
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

Input Format
The first line contains a single integer , the number of test cases.
For each test case, there are  lines.
The first line of each test case contains , the number of cubes.
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

Output Format
For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input
2
6
4 3 2 1 3 4
3
1 3 2

Sample Output
Yes
No
"""

from collections import deque

TC = int(input())
# TC = 2
possible = list(' '*TC)
for i in range(TC):
    pocet = int(input())
    # pocet = 6
    rada = deque(map(int, input().split(' ')))
    # rada = deque(map(int, '4 3 2 1 3 4'.split(' ')))
    stack = [2**32]
    for j in range(pocet):
        if rada[0] > rada[-1]:
            if rada[0] <= stack[-1]:
                stack.append(rada.popleft())
            else: possible[i] = "No"
        else:
            if rada[-1] <= stack[-1]:
                stack.append(rada.pop())
            else: possible[i] = "No"
    if possible[i] == ' ': possible[i] = "Yes"

for k in possible:
    print(k)