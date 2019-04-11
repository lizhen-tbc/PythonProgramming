# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:19:00 2019

@author: Zhen.Li
"""

from graphics import *

def main():
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at:", p.getX(), p.getY())
        
main()