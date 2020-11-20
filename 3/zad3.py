# zad3
'''Create a graph of the sine and cosine functions in the range from 0 do 3*PI. 
Evaluate where the function graphs are close to each other (distance < 0.1) and 
indicate this using points'''

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,3*np.pi,0.1)   # start,stop,step
y_sin = np.sin(x)
y_cos = np.cos(x)

distance = y_sin-y_cos
mask = np.array(np.absolute(distance)<0.1)

y_sin_close = y_sin[mask]
y_cos_close = y_cos[mask]
x_close = x[mask]

plt.figure()
plt.scatter(x_close, y_sin_close, c='red')
plt.scatter(x_close, y_cos_close, c='red')

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlim(-2,10)
plt.ylim(-1.5,1.5)
plt.yticks([-1.5, -1,-0.5,0,0.5,1,1.5])

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none') 
ax.spines['bottom'].set_position('center')
ax.spines['left'].set_position('zero')
ax.xaxis.set_ticks_position('left') 
ax.yaxis.set_ticks_position('bottom')

plt.show()

