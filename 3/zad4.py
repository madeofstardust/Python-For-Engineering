# zad4
'''Create a 500x2 matrix containing 500 2D points in the range [-1,1]^2. 
Transform the points(x, y) to points (t, r) in the polar coordinate system. 
Visualize the points as a scatter plot, such that the points are colored with 
the color map jetif the angle is t < 180  -and with the color map terrainin the 
converse case'''

import numpy as np
import matplotlib.pyplot as plt

a = np.random.uniform(low=-1, high = 1, size= 1000).reshape(500,2)
x = a[:,1]
y = a[:,0]
r = np.sqrt(x**2+y**2)
t = np.arctan2(y,x)

mask = np.array(t>0)
t_jet = t[mask]
r_jet = r[mask]

inverted_mask = np.invert(mask)
t_terrain = t[inverted_mask]
r_terrain = r[inverted_mask]

'''
plt.figure()
plt.axes(polar = True)
plt.scatter(t, r, c=r, cmap = plt.cm.jet)
plt.show()
'''

plt.figure()

plt.axes(polar = True)
plt.scatter(t_jet,r_jet, c = r_jet, cmap = plt.cm.jet)
plt.scatter(t_terrain, r_terrain, c = r_terrain, cmap = plt.cm.terrain)

plt.show()




