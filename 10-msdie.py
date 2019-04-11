# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:00:05 2019

@author: zhen.li
"""

from random import randrange

class MSDie:
    
    def __init__(self, sides):
        self.sides = sides
        self.value = 1
        
    def roll(self):
        self.value = randrange(1, self.sides + 1)
        
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
        
    