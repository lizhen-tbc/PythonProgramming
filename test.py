# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:52:13 2019

@author: zhen.li
"""

from graphics import *
from button import *

win = GraphWin("Initial Values", 200, 300)
win.setCoords(0,4.5,4,.5)

Text(Point(1,1), "Angle").draw(win)
angle = Entry(Point(2,1), 5).draw(win)
angle.setText(str(angle))

Text(Point(1,2), "Velocity").draw(win)
vel = Entry(Point(3,2), 5).draw(win)
vel.setText(str(vel))

Text(Point(1, 3), "Height").draw(win)
height = Entry(Point(3, 3), 5).draw(win)
height.setText(str(height)) 

fire = Button(win, Point(3,4), 1.25, .5, "Fire")
fire.activate()

print(fire.getLabel())