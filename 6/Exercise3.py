# Exercise 3
"""
Find a cubic spline interpolation of the points(x and y coordinates) contained 
in the fileinter1D.npz in the range 𝑥∈[−1.0,1.0]. Draw the points and the 
interpolating function.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

data = np.load('inter1D.npz')
X = data['x']
Y = data['y']

r = np.linspace(-1, 1, 12)
plt.plot(r, np.interp(r, X, Y), '--', color = 'red')

interpolation_fn = interpolate.interp1d(X, Y, kind='cubic')

g = np.linspace(-1, 1, 100)
new = interpolation_fn(g)

plt.plot(g, new, '-', color='aquamarine')

plt.show()


