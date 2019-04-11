# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:02:28 2018

@author: Zhen.Li
"""

def main():
    print("this program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)
        
main()