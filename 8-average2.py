# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:01:26 2019

@author: Zhen.Li
"""

def main():
    total = 0.0
    count = 0
    moredata = "yes"
    
    while moredata[0] == "y":
        x = float(input("Enter a number >> :"))
        total = total + x
        count = count + 1
        moredata = input("Do you have more numbers(yes or no)? ")
    
    print("\nThe average of the numbers is", total/count)
    
main()