# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:11:32 2016

@author: Miso

"""
balance = 4773
annualInterestRate = 0.2
x=0

payment = 0
balance_tmp = balance
while balance_tmp > 0:
    payment += 10
    balance_tmp = balance
    for month in range(12):
        balance_tmp = (balance_tmp-payment)*(annualInterestRate/12 + 1)  
    print(balance_tmp)    
    #x+=1
print('Lowest Payment: ' + str(payment))

#monthlyPaymentRate = 0.04   
#debt(balance, annualInterestRate, monthlyPaymentRate)

