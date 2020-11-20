# Exercise 5
'''Download the file solve.npz which contains arrays of the linear system Ax=b. 
Compute the vector x which solves this linear system or give the best 
approximation if there is none such vector.
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.load('solve.npz')

print(x.files)
A = x['A']
b = x['b']
A2 = x['A2']
b2 = x['b2']

x1 = np.linalg.solve(A,b)
c = np.linalg.lstsq(A.T, b)[0]
m2, c2 = np.linalg.lstsq(A2.T, b2)[0]

x_all = np.arange(-5, 100,5 )

plt.figure(1)
plt.subplot(211)
plt.title("Subtask 1")
plt.plot(b, x1, "o", label='datapoints', markersize=10)
'''plt.plot(x_all, c[0]*x_all**14 + c[1]*x_all**13 + c[2]*x_all**12 + c[3]*x_all**11+
         c[4]*x_all**10 + c[5]*x_all**9 + c[6]*x_all**8 + c[7]*x_all**7 + 
         c[8]*x_all**6 + c[9] * x_all**5 + c[10] * x_all**4 + c[11] * x_all**3 +
         c[12] * x_all**2 + c[13] * x_all + c[14]) '''
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none') 
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
#Subtask 2:
plt.subplot(212)
plt.title("Subtask 2")
plt.plot(x_all, m2*(x_all)+c2, 'r', label='Approximated line')
plt.legend()
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none') 
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
plt.show()

