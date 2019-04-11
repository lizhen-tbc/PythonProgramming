# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from graphics import *

def main():
    win = GraphWin("Color Window", 500, 500)
    
    # event loop: handle key presses until user presses the "q" key
    while True:
        key = win.getKey()
        if key == "q": #loop exit
            break
        
        #process the key
        if key == "r":
            win.setBackground("pink")
        elif key == "w":
            win.setBackground("white")
        elif key == "g":
            win.setBackground("lightgray")
        elif key == "b":
            win.setBackground("lightblue")
    
    win.close()
    
    
main()