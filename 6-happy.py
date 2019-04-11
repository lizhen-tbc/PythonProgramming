# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:20:53 2019

@author: Zhen.Li
"""

def happy():
    print("Happy Birthday to you!")

def sing(person):
    happy()
    happy()
    print("Happy Birthday to you, dear", person + "." )
    happy()
    
def main():
    sing("fred")
    print()
    sing("Lucy")
    
    
main()
