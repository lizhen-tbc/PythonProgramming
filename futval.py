# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:55:25 2018

@author: Zhen.Li
"""

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    
    for i in range(10):
        principal = principal * (1 + apr)
    
    print("the value in 10 years is:", principal)
    
main()