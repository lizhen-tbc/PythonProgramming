# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:19:20 2019

@author: Zhen.Li
"""

import math
def main():
    print("This program finds the real solutions to a quadratic\n")
    
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("enter coefficient c: "))
        
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot)/(2*a)
        root2 = (-b - discRoot)/(2 * a)
        print("\nThe solutions are:", root1, root2)
        
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("\nThe equation has no real roots!")
        else:
            print("Invalid coefficient given")
        
    except: 
        print("\nSomething went wrong.")
    
        
main()