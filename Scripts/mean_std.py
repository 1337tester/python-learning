# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 08:59:19 2016

@author: Miso
"""
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std
    
def coef_of_var(X):
    mean_std = getMeanAndStd(X)
    print('mean ', mean_std[0])
    print('standard deviation ', mean_std[1])
    return mean_std[1]/mean_std[0]
    
    
x = [6,5,7,6]

y = [2,1,3,2]

print(coef_of_var(x))
print(coef_of_var(y))