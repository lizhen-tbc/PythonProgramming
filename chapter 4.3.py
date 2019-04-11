# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:24:08 2018

@author: Zhen.Li
"""

from graphics import *

win = GraphWin('Shapes')
center = Point(100, 100)
circ = Circle(center, 30)
circ.setFill('red')

circ.draw(win)

label = Text(center, "Red Circle")
label.draw(win)

rect = Rectangle(Point(30, 30), Point(70, 70))
rect.draw(win)

line = Line(Point(20, 30), Point(180, 165))
line.draw(win)

oval = Oval(Point(20, 150), Point(180, 199))
oval.draw(win)