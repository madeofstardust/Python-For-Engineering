# Exercise 2
"""
Create a 3D plot of the 2D histogram from the previous exercise. 
Generate a mesh grid for x and y from 0 to 100 with the linspaceand meshgrid 
functions. Use the plot_surface function with the color map “jet” to visualize 
the 3D plot.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
import numpy as np

X = np.load('daneX.npy')
Y = np.load('daneY.npy')

H, _, _ = np.histogram2d(X, Y, bins=100)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_axes = np.arange(0, 100, 1)
y_axes = np.arange(0, 100, 1)
X, Y = np.meshgrid(x_axes, y_axes)

ax.plot_surface(X, Y, H, cmap='jet')

plt.show()

