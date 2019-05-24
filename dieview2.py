# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:51:43 2019

@author: zhen.li
"""

from graphics import *

class DieView:
    """ DieView is a widget that displays a graphical representation of as 
    standard six-sided die. """
    
    def __init__(self, win, center, size):
        
        
        # first define some standard values
        self.win = win
        self.background = "white"  # color of die face
        self.foreground = "black"  # color of the pips
        self.psize = 0.1 * size    # radius of each pip
        hsize = size/2.0           # half of size
        offset = 0.6 * hsize       # distance from center to outer pips
        
        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)
        
        #create 7 circles for standard pip locations
        self.pips = [self.__makePip(cx - offset, cy - offset),
                     self.__makePip(cx - offset, cy),
                     self.__makePip(cx - offset, cy + offset),
                     self.__makePip(cx, cy),
                     self.__makePip(cx + offset, cy - offset),
                     self.__makePip(cx + offset, cy), 
                     self.__makePip(cx + offset, cy + offset)]
        
        # create a table for which pips are on for each value
        self.onTable = [ [], [3], [2,4], [2,3,4], [0,2,4,6],
                        [0,2,3,4,6], [0,1,2,4,5,6]]
        
        self.setValue(1)
        
    def __makePip(self, x, y):
        """internal helper method to draw a pip at (x,y)"""
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip
    
    def setValue(self, value):
        """ set this die to display value"""
        for pip in self.pips:
            pip.setFill(self.background)
            
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)
        
        
        







