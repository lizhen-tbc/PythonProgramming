# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:06:39 2019

@author: Zhen.Li
"""

def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the unicode encoding of the mssage.\n")
    
    message =  input("Please enter the message to encode:")
    
    print("\nHere are the unicode codes:")
    
    for ch in message:
        print(ord(ch), end = " ")
        
main()