# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:06:25 2016

@author: Miso
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    max_len = []
    for n in range(len(L)):
        num = n + 1
        local_up = [L[n]]
        local_down = [L[n]]
        while num < len(L):
            if L[num] > local_up[-1]:
                local_up.append(L[num])
                if len(local_down) > len(max_len):
                    max_len = local_down[:]
                local_down = [L[num]]
            elif L[num] < local_down[-1]:
                local_down.append(L[num])
                if len(local_up) > len(max_len):
                    max_len = local_up[:]
                local_up = [L[num]]
            elif L[num] == local_down[-1]:
                local_down.append(L[num])
                local_up.append(L[num])
            num += 1
        if len(local_down) > len(max_len):
            max_len = local_down[:]
        elif len(local_up) > len(max_len):
            max_len = local_up[:]
    return sum(max_len)
#    return max_len
    

#L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
#print(longest_run(L))
print('je 45 == ' + str(longest_run([1, 2, 3, 4, 5, 6, 7, 8, 9])))
print('je 6 == ' + str(longest_run([1, 2, 3, 2, 1])))
print('je 3 == ' + str(longest_run([1, 2, 1, 2, 1, 2, 1, 2, 1])) )
print('je 15 == ' + str(longest_run([1, 2, 3, 4, 5, 0, 10, 1, 2, 3, 4, 5])) )
print('je 65 == ' + str(longest_run([1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])))
print('je 6 == ' + str(longest_run([1, 2, 3, 2, -1])))
print('je 4 == ' + str(longest_run([3, 2, -1, 2, 7])))
print('je -6500 == ' + str(longest_run([100, 200, 300, -100, -200, -1500, -5000])))
print('je 1000 == ' + str(longest_run([100, 200, 300, 400, 0, 10000, 20000])))
print('je -6 == ' + str(longest_run([1, 2, 3, 2, -1, -10])))
print('je 11 == ' + str(longest_run([3, 3, 3, 3, 3, 3, 3, -10, 1, 2, 3, 4])))
print('je 348 == ' + str(longest_run([3, 4, 5, 6, 10, 20, 100, 200, 1, 3, 3, 3, -10, 1, 2, 3, 4])))
print('je 15 == ' + str(longest_run([3, 3, 3, 3, 3])))
print('je -15 == ' + str(longest_run([-3, -3, -3, -3, -3])))
print('je 7 == ' + str(longest_run([1, 2, 3, 2, 1, -10, -20, 3, 3, 3, 3, 3, 3, 3, 3, 3])))
print('je 45 == ' + str(longest_run([1, 2, 3, 2, 1, -10, -20, 3, 4, 5, 7, 7, 8, 9, 11, 11])))
print('je 11078 == ' + str(longest_run([-10, -9, -8, -7, -6, -5, -3, -1, 1, 3, 5, 8, 10, 100, 1000, 10000])))
print('je -111439 == ' + str(longest_run([-1, -2, -3, -4, -10, -100, -150, -169, -1000, -10000, -100000])))
print('je 11130 == ' + str(longest_run([1, 1, 2, 3, 5, 8, 10, 100, 1000, 10000])))
print('je 111134 == ' + str(longest_run([100000, 10000, 1000, 100, 10, 8, 8, 5, 2, 1, 0])))
print('je 6 == ' + str(longest_run([1, 2, 3, 2, 1, 10, 100, 50, 20, 1000, 10000, 5000, 2000, 100000, 200000, 150000, 100000])))
print('je 450000 == ' + str(longest_run([100000, 150000, 200000, 100000, 2000, 5000, 10000, 1000, 20, 50, 100, 10, 1, 2, 3, 2, 1])))
print('je 170 == ' + str(longest_run([100, 10, 10, 10, 10, 10, 10, 10, 0])))
print('je -170 == ' + str(longest_run([-100, -10, -10, -10, -10, -10, -10, -10, 0])))
print('je 161 == ' + str(longest_run([1, 10, 10, 10, 10, 10, 10, 100])))
print('je -161 == ' + str(longest_run([-1, -10, -10, -10, -10, -10, -10, -100])))
print('je 1500100 == ' + str(longest_run([1, 2, 1, 2, 1, 2, 1, 2, -1, -2, -1, -2, 10, 20, 10, 20, 100, 200, 100, 0, 100, 0, 100, 0, 0, 100, 0, 0, 0, 100, 1500000, -1500000, 1, -150001])))
