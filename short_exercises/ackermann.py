# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 01:20:48 2017

@author: Miso
"""

def ack(m,n):
    result = 0
    if (m == 0): result = n+1
    elif (n == 0): result = ack(m-1,1)
    else: result = ack(m-1, ack(m,n-1))    
    return result
    
    
for i in range(4):
    for j in range(4):
        print("Ackerman(%s, %s) = " % (i, j), ack(i,j))
#print(ack(3,5))
