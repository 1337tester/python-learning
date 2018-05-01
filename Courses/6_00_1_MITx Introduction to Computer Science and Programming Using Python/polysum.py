# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 16:03:03 2016

@author: Miso
"""
import math

def polysum(n, s):
    '''
    returns the sum of the area and 
    square of the perimeter of the regular polygon
    rounded to 4 decimal places
    arg ->  n is number of sides
            s is lenght of each side
    '''
    area = (0.25*n*s*s)/(math.tan(math.pi/n))
    boundary_square = (s*n)**2
    return round(area + boundary_square,4) 