# Exercise 4
"""
a) Open the file inter2D.npz and visualize the data as a 3D wireframe plot(plot_wireframe)
b) Find a smoother (increase stride) cubic 2D spline interpolation for these data 
points (x, y and z coordinates)in the range 𝑥,𝑦 ∈[0,10]and visualize the result  
as a 3D plot
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate

data = np.load('inter2D.npz')
X = data['x']
Y = data['y']
Z = data['z']

x, y = np.meshgrid(X, Y)

f = interpolate.interp2d(X, Y, Z, kind='cubic')
new_x = np.linspace(0, 10, 50)
new_y = np.linspace(0, 10, 50)
new_z = f(new_x, new_y)
new_x, new_y = np.meshgrid(new_x, new_y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, Z)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(new_x, new_y, new_z, cmap='jet')
plt.show()