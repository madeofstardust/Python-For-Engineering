# EX 1
"""
Plot a vector field and a stream plot for the exponential growth model.
•At the start of an experiment there are 10 plants of Wolffiamicroscopica. 
At time = 240 hours there are 1015. How many plants will there be at 20 days? 
Model the population growth assuming a constant exponential growth rate and plot 
the graph using logarithmic scale.
"""
import numpy as np
import matplotlib.pyplot as plt

# P(t) = C*e^(Kt)
# P - population at given time, t - time, C - starting population, K - growth koefficient


def exp_growth(t, C=10, K=0.03):
    t = np.arange(0, t, 1)
    exp = np.exp(K*t)
    P = (C*exp).astype(float)
    return P, t

# a)
K = 0.03
C = 10
population, time = exp_growth(200, C, K)

xx, yy = np.meshgrid(np.linspace(0,200,10),np.linspace(0,4000,20))

def function(t):
    result = C *np.exp(K*t)
    return result

def dif_eq(x):
    result = C * np.exp(K*x)
    return result


dxdt = dif_eq(xx)
dt = 0.1* np.ones(xx.shape)
dx = dxdt* (dt)
plt.figure()
plt.title("vector field")
plt.ticklabel_format(style ='plain')
plt.plot(time, population)
plt.quiver(xx, yy, dt, dx, angles='xy', scale=50)
plt.show()


U = -1 - xx**2 + yy
V = 1 + xx - yy**2

plt.figure()
plt.title("stream plot")
plt.ticklabel_format(style ='plain')
plt.streamplot(xx,yy,dt,dx)
plt.plot(time, population)

plt.show()

# b)
''' 
t= 0,   P = 10,    C = 10
t= 240, P = 1017   1017 = 10e^(240*K)
                   101,7 = e^(240*K)
                   K = ln(101)/240
'''
t = np.arange(0, 500, 1)
C = 10
K2 = (np.log(101))/240
exp_2 = np.exp(K2*t)
P_2 = C*exp_2
P_2 = P_2.astype(float)

new_pop, new_t = exp_growth(500, C, K2)

plt.figure()
plt.ticklabel_format(style ='plain')
plt.plot(t ,P_2)
plt.scatter(new_t[239], new_pop[239])
plt.show()

