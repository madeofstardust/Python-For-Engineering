# Exercise 2:
'''
a)Create a bivariate distribution (normal with mu=1, sigma=1) and visualize
it as a scatter plot. You should see a point cloud centered around the origin.

b) Apply a transformation along the x-axis via a scaling matrix that stretches 
the point cloud of data by a factor 3 and visualize the points again.

c) Rotate the point cloud by 45 degrees “up” using a rotation matrix.

d)How can you apply both transformations (scaling and rotating) in a single 
transformation? 

e) Calculate the SVD of your transformed bivariate data sample. 
Create the rotation and scaling matrices from the output of the svd function. Transform 
your  data set with the inverse of the aggregated scaling and rotation matrices 
(T=(RS)-1). Plot the new data as a scatter plot, you should see a similar point 
cloud to the original one again. 
What is the relationship between eigenvalues and singular values obtained by SVD?
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# a)
m = np.array([0,0])
cov = np.array([[1,0],[0,1]])
x, y = np.random.multivariate_normal(m, cov, 1000).T
plt.figure()
plt.title("Bivariate distribution:")
plt.plot(x, y, '.', color = 'lightcoral')
plt.show()

# b)

spread_scale = np.array([[3, 0], [0, 1]])
spread_cov = np.dot(cov, spread_scale)
x2, y2 = np.random.multivariate_normal(m, spread_cov, 1000).T
plt.figure()
plt.title("Spreading:")
plt.plot(x2, y2, '.', color = 'mistyrose')
plt.plot(x, y, '.', color = 'lightcoral')
plt.show()

# c)
rotate_scale = np.array([[0.70, 0.70],[-0.70, 0.70]])

rotate_cov = np.dot(cov, rotate_scale)
x3, y3 = np.random.multivariate_normal(m, rotate_cov, 1000).T
plt.figure()
plt.title("Rotation:")
plt.plot(x, y, '.', color = 'lightcoral')
plt.plot(x3, y3, '.', color = 'peachpuff')
plt.show()

# d)

rotate_spread_cov = np.dot(spread_cov, rotate_scale)
x4, y4 = np.random.multivariate_normal(m, rotate_spread_cov, 1000).T
plt.figure()
plt.title("Spreading and Rotation:")
plt.plot(x2, y2, '.', color = 'lightcoral')
plt.plot(x4, y4, '.', color = 'peachpuff')
plt.show()

# e)
matrix = np.column_stack((x4,y4))
df_matrix = pd.DataFrame(matrix)
u, s, vh = np.linalg.svd(matrix, full_matrices = False)
act_s = np.array([[s[0], 0],[0, s[1]]])
df_u = pd.DataFrame(u)
df_s = pd.DataFrame(s)
df_act_s = pd.DataFrame(act_s)
df_vh = pd.DataFrame(vh)

#matrix = u*s*v.T
step_1 = np.dot(u, act_s)
df_step_1 = pd.DataFrame(step_1)
step_2 = np.dot(step_1, vh)

'''
I have no idea how to compute the rotation matrices. We did not cover that on
Linear algerba, nor numerical methods, and I cannot find any explanation online.
Could You please explain this issue?
'''

'''
If we think about the matrix U as telling us something about specific concepts,
then the eigenvalues are the strength of each concept.
'''
