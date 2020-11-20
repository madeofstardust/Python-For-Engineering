# Exercise 5
'''Project the data from 3D to 2D and visualize the result on another plot 
(multiply the data with a 3x2 matrix constructed from the two largest eigenvectors 
–alternatively use SVD). Compare your results to the PCAmethod from the module 
matplotlib.mlabor sklearn
'''
import matplotlib.pyplot as plt
import numpy as np

ds = np.loadtxt('measure.txt')
cov = np.cov(ds)

# eigenvalues, egienvectors:
_, v = np.linalg.eig(cov)

matrix = np.dot(v[::2], ds)

plt.scatter(matrix[0], matrix[1])
plt.show()

