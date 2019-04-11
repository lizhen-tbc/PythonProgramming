# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:01:26 2019

@author: Zhen.Li
"""

def main():
    fileName = input("What file are the numbers in?")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0
    for line in infile:
        total = total + float(line)
        count = count + 1
        
    print("\nThe average of the numbers is", total / count)


    
main()