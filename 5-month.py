# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:34:49 2019

@author: Zhen.Li
"""

def main():
    month_ = eval(input("Please enter month:"))
    
    monthstring = "JanFebMarAprMayJunJulAugSepOctNovDec"
    
    month_abb = monthstring[month_ * 3 - 3 : month_ * 3]
    
    print("abbreviation is :", month_abb)
    
    
main()