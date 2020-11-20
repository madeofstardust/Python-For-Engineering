# Exercise 1
"""
Download the files X and Y containing two parameters representing some real 
world data. Create a 2D histogram of these two data samples – visualize them as 
an image andas a contour plot. Use the function histogram2D to create a 2D 
histogram. Draw a color bar.
"""
import matplotlib.pyplot as plt
import numpy as np

X = np.load('daneX.npy')
Y = np.load('daneY.npy')

H, xedges, yedges = np.histogram2d(X, Y, bins=100)

plt.figure()
plt.pcolormesh(H, cmap='jet')
plt.colorbar()
plt.show()



