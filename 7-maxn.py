# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:46:28 2019

@author: Zhen.Li
"""

def main():
    n = int(input("How many numbers are there?"))
    
    #set max to be the first value
    maxval = float(input("Enter a number >> "))
    
    #Now compare the n-1 successive values
    for i in range(n-1):
        x = float(input("Enter a number >> "))
        if x > maxval:
            maxval = x
            
    print("The largest value is", maxval)
    
main()