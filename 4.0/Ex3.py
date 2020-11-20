# Exercise 3:
'''Create a plot of the conditioning number with variable p for the following 
linear system (p ε[0.9, 1.1]):
    
 x1 + sqrt(p)x2 = 1
 x1 + (1/sqrt(p))x2 = 2    
    
What is the result of your numerical analysis?
'''
import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt
import pandas as pd

p = np.arange(0.9, 1.11, 0.01)
a = np.array([[1,1],[sqrt(p), 1/sqrt(p)]])
A = a.T
b = ([1,2])
df = pd.DataFrame(A)

P_1 = A[0,1]
P_2 = A[1,1]
condition_numbers = np.zeros(22)

for i in range(len(P_1)):
    matrix_a = np.array([[1,1],[P_1[i], P_2[i]]])
    matrix_A = matrix_a.T
    condition_numbers[i] = np.linalg.cond(matrix_A)

plt.figure()
plt.scatter(p, condition_numbers)
# this shows that the parameter p must be equal to one.
plt.show()



