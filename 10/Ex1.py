# Ex1:

'''
Exercise 1 (2 points)
•Create a temporal simulation of a ball moving on a horizontal line from one 
side of the screen to the other. Formulate appropriate differential equations 
describing the rate of change of position for the ball and solve them. Use the 
solution to update ball positions in each time step.

'''

from vpython import *
import numpy as np

direction = 1
t=0
dt=0.01
g=vector(0,-9.8,0)

ball = sphere(pos=vector(-100,5,0), radius=3, color=color.cyan)
ball.v=vector(1,0,0)

#floor=box(pos=vector(-100,0,0), length=200, width=2, height=.1, color=color.white)
myArrow = arrow(pos=vector(-100,0,0), axis=vector(1,0,0), length = 200, shaftwidth = 1)

while True:
    if direction == 1:
        ball.pos=ball.pos+ball.v*dt
    else:
        ball.pos=ball.pos-ball.v*dt
    t=t+dt
    print(ball.pos)
    if ball.pos.x>100:
        direction = -1
    if ball.pos.x < -100:
        direction = 1
