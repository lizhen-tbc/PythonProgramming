# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:42:28 2019

@author: Zhen.Li
"""

def main():
    print("please enter the count of each coin type.")
    quarters = int(input("Quarters:"))
    dimes = int(input("dimes:"))
    nickels = int(input("nickels:"))
    pennies = int(input("pennies:"))
    
    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies
    
    print("The total is  ${0}.{1:>2}".format(total//100, total%100))
    
main()