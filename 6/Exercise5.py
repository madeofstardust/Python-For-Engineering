# Exercise 5
"""
Reconstruct the image using an interpolation method of your choice. 
Which person is depicted in the image? 
"""
import imageio
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from scipy import interpolate
input_image = imageio.imread('face.png')
input_image.shape
(512, 512, 3)
imageio.imwrite('face.png', input_image) 

plt.figure()
plt.imshow(input_image, cmap=plt.cm.gray)
plt.show()

y = []
x = []
for i in range (0, 200):
    for j in range (0, 200):
        if input_image[i,j] > 150:
            x.append(i)
            y.append(j)
            
            
#mask invalid values
array = np.ma.masked_invalid(array)
xx, yy = np.meshgrid(x, y)
#get only the valid values
x1 = xx[~array.mask]
y1 = yy[~array.mask]
newarr = array[~array.mask]

GD1 = interpolate.griddata((x1, y1), newarr.ravel(),
                          (xx, yy),
                             method='cubic')
