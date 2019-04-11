# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:30:46 2019

@author: Zhen.Li
"""

def main():
    celsius = float(input("What is the Celsius temperature?"))
    farenheit = 9/5*celsius + 32
    print("The temperature is",farenheit, "degrees Fahrenheit.")
    
    #print warnings for extreme temps
    if farenheit > 90:
        print("It's really hot out there. Be careful!")
    if farenheit < 30:
        print("Brrrrr. Be sure to dress warmly!")
        
main()        
        