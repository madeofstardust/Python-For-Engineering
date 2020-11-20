# Exercise 1: 
'''Create a plot of the following system of equations: •What can you observe?
•Compute the rank and conditioning number of matrix A which expresses the above
 system of equations.
2(x1)+3(x2) = 4
5(x1)+4(x2) = 23
 •Solve the system of equations and give the LU decomposition of matrix A.
 You can verify the correctness of your solution with the graph you have drawn 
 –is this always possible? '''

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

a = np.array([[2,5], [3,4]])
A = a.T
b = np.array([4,23])
x = np.linalg.solve(A, b)
print(x)

x1 = np.arange(-10, 10, 1)

X1 = (4.0-3.0*x1)/2.0
X1_2 = (23.0-4.0*(x1))/5.0

X2 = (4-2*x1)/3
X2_2 = (23-5*x1)/4


plt.figure()
plt.plot(x1, X1)
plt.plot(x1, X1_2)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none') 
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

plt.show()

#rank:
rank = np.linalg.matrix_rank(A)

# condition number:
cnd = np.linalg.cond(A)

# LU decomposition:
(P, L, U) = linalg.lu(A)
print ("LU decomposition: P =\n",P,"\n L =\n", L,"\n U =\n", U)
