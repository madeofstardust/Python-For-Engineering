# Exercise 2:
'''•Add another equation 5x2= 18 to the system of equations of the previous 
exercise and visualize it on the plot.
•Does another solution exist? 
•Compute/approximate the solutionas best as possible (minimalizing the square 
error).'''
'''2(x1)+3(x2) = 4
5(x1)+4(x2) = 23
5x2 = 18'''
import numpy as np
import matplotlib.pyplot as plt
#Arrays:
a = np.array([[2,5,0], [3,4,5]])
b = np.array([4,23,18])
# We cannot use solve(), as it demands the matrix to be of equal rows and columns
x = np.linalg.lstsq(a.T, b)
print("Coordinates of least squares solution: ",x[0])

x1 = np.arange(-10, 10, 1)

X2 = (4-2*x1)/3
X2_2 = (23-5*x1)/4
X2_3 = np.full((20, 1), 18/5)

plt.figure()
plt.plot(x1, X2, label="First equation")
plt.plot(x1, X2_2, label="Second equation")
plt.plot(x1, X2_3, label="Third equation")
plt.scatter(1.42, 3.13, label="Approximated value")
plt.legend()
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none') 
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

plt.show()
                                                      


