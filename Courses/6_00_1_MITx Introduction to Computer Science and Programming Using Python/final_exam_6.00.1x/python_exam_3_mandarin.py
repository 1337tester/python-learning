# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 10:19:06 2016

@author: Miso
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
          
          
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    mandarin_num = ''
    us_int = int(us_num)
    if 0 <= us_int <= 10:
        mandarin_num = trans[us_num]
    elif 10 < us_int < 20:
        mandarin_num = trans['10'] + ' ' + trans[str(us_int % 10)]
    elif 20 <= us_int <= 99:        
        if us_int % 10 != 0:
            mandarin_num = trans[str(us_int // 10)] + ' ' + trans['10'] + ' ' + trans[str(us_int % 10)]
        else:
            mandarin_num = trans[str(us_int // 10)] + ' ' + trans['10']         
    return mandarin_num
    
    
    
    
    
    
for x in range(-5,120):
    print(convert_to_mandarin(str(x)), end=", ")
    
    
print()
print(convert_to_mandarin('30'))