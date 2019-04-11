# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:30:38 2019

@author: Zhen.Li
"""

def main():
    dateStr = input("Enter a date: ")
    mm, dd, yy = dateStr.split("/")
    
    mm = int(mm)
    
    months = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" ,
              "Jul" , "Aug" , " Sep" , "Oct" , "Nov" , "Dec" ]
    
    print(months[mm-1], dd + ",", yy)
    
main()