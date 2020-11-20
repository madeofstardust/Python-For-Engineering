# Exercise 3
'''
a) Visualize measurements of the flowers of ludwiga octovalvis on 3D plot. 
b) Compute  the means and the covariance matrix as well as the correlation 
matrix– what can  you say about the relations of the 3 parameters: sepal length, 
petal length and sepal width?
'''
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('measure.txt')
# means:
m = [np.mean(data[0]), np.mean(data[1]), np.mean(data[2])]

# correlation matric:
cor = np.corrcoef(data)

# covariance matrix:
cov = np.cov(data)

#a)
plt.figure()
plt.subplot(111, projection='3d')
plt.plot(data[0], data[1], data[2], '.', )
plt.show()