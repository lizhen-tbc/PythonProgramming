# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:01:26 2019

@author: Zhen.Li
"""

def main():
    total = 0.0
    count = 0
    x = float(input("Enter a number (negative to quit) >> "))
    
    while x >= 0:
        
        total = total + x
        count = count + 1
        x = float(input("Enter a number (negative to quit) >> "))
    
    print("\nThe average of the numbers is", total/count)
    
main()