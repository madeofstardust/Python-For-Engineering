# Ex2
"""
Exercise 2 (3 points)
•Read the tutorial on simulating simple pendulum motion 
http://techforcurious.website/simulation-of-pendulum-vpython-tutorial-visual-python/.
•Reimplementthe pendulum motion simulation described in the tutorial twice by 
using ode_int AND solve_ivp to solve the differential equations instead of the 
Forward Euler method. Choose an appropriately larger time step compared to the 
one used in the tutorial. How could we make the animation smoother?
•Report the
 averaged runtime for 1000 simulations for all solvers (including the Forward 
 Euler method) using timeit assuming the LSODA method for solve_ivp. Did your
 scripts perform better than the tutorial benchmark?
"""



#%%
from vpython import*

display(width=600,height=600,center=vector(0,12,0),background=color.white)
g=9.8 # acceleration due to gravity
bob=sphere(pos=vector(5,2,0),radius=0.5,color=color.white)
pivot=vector(0,20,0)
roof=box(pos=pivot,size=vector(10,0.5,10),color=color.green)
rod=cylinder(pos=pivot,axis=bob.pos-pivot,radius=0.1,color=color.red)

t=0 # time 
dt=0.01 # time interval 

l=mag(bob.pos-pivot) # length of pendulum
cs=(pivot.y-bob.pos.y)/l # calculation of cos(theta) 
theta=acos(cs) # angle with vertical direction
vel=0.0 # angular velocity

##Euler method:
while (t<100):
    rate(100) # maximum 100 calculations per second
    acc=-g/l*sin(theta) # updating of angular acceleration
    theta=theta+vel*dt # updating of angular position
    vel=vel+acc*dt # updating of angular velocity
    bob.pos=vector(l*sin(theta),pivot.y-l*cos(theta),0) # cal. position
    rod.axis=bob.pos-rod.pos # updating other end of rod of pendulum
    t=t+dt # updating time

#%%'
    # Using ODE_int
from vpython import*
import vpython as vp
import numpy as np
from scipy import integrate
from scipy import *
from matplotlib.pyplot import *

def pend(y, t, b, c):
    return np.array([y[1], -b*y[1] -c*np.sin(y[0])])

y0 = np.array([np.pi-0.1, 0.0]) #initialvalue
b=0.01
g=9.8
t = np.linspace(0, 20, 400) #
dt=0.01 # time interval 

pendulum = integrate.odeint(pend, y0, t, args=(b, g))

display(width=600,height=600,center=vector(0,12,0),background=color.white)
g=9.8 # acceleration due to gravity
bob=sphere(pos=vector(5,2,0),radius=0.5,color=color.white)
pivot=vector(0,20,0)
roof=vp.box(pos=pivot,size=vector(10,0.5,10),color=color.green)
rod=cylinder(pos=vector(pivot),axis=bob.pos-pivot,radius=0.1,color=color.red)

l=mag(bob.pos-pivot) # length of pendulum
cs=(pivot.y-bob.pos.y)/l # calculation of cos(theta) 
theta=acos(cs) # angle with vertical direction
vel=0.0 # angular velocity

#while (t<100):
for i in range(400):
    vp.rate(100) # maximum 100 calculations per second
    acc=-g/l*sin(theta) # updating of angular acceleration
    theta=theta+vel*dt # updating of angular position
    vel=vel+acc*dt # updating of angular velocity
    bob.pos=vector(pendulum[i, 0],pendulum[i, 1], 0) # cal. position
    print(bob.pos)
    rod.axis=bob.pos-rod.pos # updating other end of rod of pendulum
    t=t+dt # updating time
    
#%%
   # Using solve_ivp
   
from vpython import*
import vpython as vp
import numpy as np
from scipy import integrate
from scipy import *
from matplotlib.pyplot import *

def pend(y, t, b, c):
    return np.array([y, -b*y -c*np.sin(y)])

y0 = np.array([np.pi-0.1, 0.0]) #initialvalue
b=0.01
g=9.8
t = np.linspace(0, 20, 400) #
dt=0.01 # time interval 

pendulum = integrate.solve_ivp(pend, t, y0, args=(b, g))
   
display(width=600,height=600,center=vector(0,12,0),background=color.white)
g=9.8 # acceleration due to gravity
bob=sphere(pos=vector(5,2,0),radius=0.5,color=color.white)
pivot=vector(0,20,0)
roof=vp.box(pos=pivot,size=vector(10,0.5,10),color=color.green)
rod=cylinder(pos=vector(pivot),axis=bob.pos-pivot,radius=0.1,color=color.red)

l=mag(bob.pos-pivot) # length of pendulum
cs=(pivot.y-bob.pos.y)/l # calculation of cos(theta) 
theta=acos(cs) # angle with vertical direction
vel=0.0 # angular velocity

#while (t<100):
for i in range(400):
    vp.rate(100) # maximum 100 calculations per second
    acc=-g/l*sin(theta) # updating of angular acceleration
    theta=theta+vel*dt # updating of angular position
    vel=vel+acc*dt # updating of angular velocity
    bob.pos=vector(pendulum[i+1, 0],pendulum[i+1, 1], 0) # cal. position
    print(bob.pos)
    rod.axis=bob.pos-rod.pos # updating other end of rod of pendulum
    t=t+dt # updating time