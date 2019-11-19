#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    bra = list(s)
    while len(bra)>0:
        changed = 0
        for i in range(len(bra)-1):
            if match_brackets(bra[i], bra[i+1]):
                del bra[i+1], bra[i]
                changed = 1
                break
        if changed == 0: return 'NO'
    if len(bra) == 0: return 'YES'

def match_brackets(left, right):
    if left == '{' and right == '}': return True
    if left == '[' and right == ']': return True
    if left == '(' and right == ')': return True
    return False

def test_balance_easy(): assert isBalanced('{[()]}') == 'YES'
def test_balance_negative(): assert isBalanced('{[(])}') == 'NOo', 'aaa'
def test_balance_complex(): assert isBalanced('{(([])[])[]}') == 'YES'
# def test_balance_fail(): assert isBalanced('{(([])[}') == 'YES'
