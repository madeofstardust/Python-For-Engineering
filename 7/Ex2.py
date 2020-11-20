# Ex 2
"""
Plot a vector field and a stream plot for the logistic growth model. Express 
the rate of change of population size with a color map.
•Bacteria grow at a rate of 20 per hour in a petri dish. 
If there is initially one bacterium and a carrying capacity of 1 million cells, 
how long does it take to reach 500,000 cells? Plot the graph using logarithmic scale
"""
import numpy as np
import matplotlib.pyplot as plt

'''
Logistic growth:
    
    N(t) = c_0/n_0 + alfa*exp(-kt)
    alfa - constant

    Bacteria at time 0 = N(0) = 1

    c/1-alfa = n_0
'''


t = np.arange(0,20,1)
alfa = 999999
k = 1.8
c_0 = 1000000
n_0 = 1
def log_growth(t = t, alfa = alfa, k = k, c_0 = c_0, n_0 = n_0):
    result = c_0/(n_0+alfa*np.exp(-k*t))
    return result

result = log_growth()

plt.figure()
plt.plot(t, result)
plt.show()

xx, yy = np.meshgrid(np.linspace(0,20,10),np.linspace(0,1000000,10))


dxdt = log_growth(t = xx)
dt = 0.001* np.ones(xx.shape)
dx = dxdt* (dt)

plt.figure()
plt.title("vector field")
plt.ticklabel_format(style ='plain')
plt.plot(t, result)
plt.quiver(xx, yy, dt, dx, angles='xy', scale=100)
plt.show()

plt.figure()
plt.title("stream plot")
plt.ticklabel_format(style ='plain')
plt.streamplot(xx,yy,dt,dx)
plt.plot(t, result)
plt.show()

