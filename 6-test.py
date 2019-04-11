# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 15:49:28 2019

@author: Zhen.Li
"""

#def addInterest(amount, rate):
#    for i in range(len(amount)):
#        amount[i] = amount[i] * (1 + rate)
#        
#def test():
#    amounts = [1000, 2200, 900, 360]
#    rate = 0.05
#    addInterest(amounts, rate)
#    print (amounts)
#    
    
def addInterest(balance, rate):
    newBalance = balance * (1 + rate)
    balance = newBalance
    return(balance)
    
def test():
    amount = 10000
    rate = 0.05
    amount = addInterest(amount, rate)
    print(amount)