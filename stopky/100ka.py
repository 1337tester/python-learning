# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:29:36 2016

@author: Miso
"""

x=100
print('Ostava ti este ' + str(x))
while x>0:
    a = input('Kolko si dal?:')
    if a == 'reset':
        x = 100
        print('Ostava ti este ' + str(x))
    elif a == 'exit':
        print('Koniec')
        break
    x-=int(a)
    print('Ostava ti este ' + str(x))

print ('Tadaaaaa')