#Exercise 4
'''
•Load data from the files x and y to an ndarray. Create the Vandermonde
matrix A of polynomials of 1st order for the data sample x. Compute the least 
squares approximation of the linear system Ax = y. Visualize the data as 
points x,y and draw the solution of the approximation(the solution is a 
straight line).
•Create an polynomial approximation of 2nd order for the above linear system 
(change the Vandermonde matrix to one that is an order higher).
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import sqrt
from numpy.polynomial import polynomial as P

x = np.load('pom_x.npy')
y = np.load('pom_y.npy')
ones = np.ones(15)
x = x.astype(np.float64)
V = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(V, y, rcond=None)[0]

#subtask 2:
x_sq = x*x
V2 = np.vstack([x, np.ones(len(x)), np.ones(len(x))]).T
V2_sq = np.vstack([x_sq, x, np.ones(len(x))]).T
m2, n2, c2 = np.linalg.lstsq(V2_sq, y, rcond=None)[0]

equation = m2*(x_sq)+n2*x+c2

plt.figure(1)
plt.subplot(211)
plt.subplots_adjust(hspace=0.5, wspace=0.4)
plt.title("Linear equation approximation:")
plt.plot(x, y, 'o', label='Points', markersize=10)
plt.plot(x, m*x + c, 'g', label='Approximated line')
plt.legend()

plt.subplot(212)
plt.title("Quadratic equation approximation")
x_all = np.linspace(15, 75, 1000)
x_all_sqrt = x_all**2
plt.plot(x, y, 'o', label='Points', markersize=10)
plt.plot(x_all, m2*(x_all_sqrt) + n2*x_all+c2, 'g', label='Approximated line')
plt.legend()
plt.show()

