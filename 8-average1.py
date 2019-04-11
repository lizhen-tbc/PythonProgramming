# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:28:07 2019

@author: Zhen.Li
"""

def main():
    n = int(input("How many numbers do you have?" ))
    total = 0.0
    for i in range(n):
        x = float(input("Enter a number >> "))
        total = total + x
    print("\n The average of the numbers is", total/n)
    
main()