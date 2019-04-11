# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:00:05 2019

@author: zhen.li
"""

from math import sin, cos, radians

def main():
    angle = float(input("Enter the launch angle (in degrees): "))
    vel = float(input("Enter the initial velocity (in meters/sec): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculations: "))
    
    #convert angle to radians
    theta = radians(angle)
    
    #set the initial position and velocities in x and y directions
    xpos = 0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    
    while ypos >= 0.0:
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1)/2.0
        yvel = yvel1
        
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))
    
main()
