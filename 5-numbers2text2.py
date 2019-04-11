# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:47:36 2019

@author: Zhen.Li
"""

def main():
    instring = input("please enter the unicode-encoded message: ")
    
    message = []
    
    for numstr in instring.split():
        codeNum = int(numstr)
        message.append(chr(codeNum))
    
    message = "".join(message)
    print(message)
    
main()