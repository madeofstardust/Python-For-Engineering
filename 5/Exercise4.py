# Exercise 4
'''
Calculate eigenvectors and eigenvalues of the covariance matrix. Visualize the 
vectors originating at the data mean (code). To reduce the dimensionality of 
the data from three to two dimensionswhat subspace will preserve most information?
'''

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch

data = np.loadtxt('measure.txt')

# covariance matrix:
cov = np.cov(data)

#eigenvalues, egienvectors
w, v = np.linalg.eig(cov)

v_1 = v[:,0]
v_2 = v[:,1]
v_3 = v[:,2]



#means:
m = np.empty((3, 1))
np.append(m, np.mean(data[0]))
np.append(m, np.mean(data[1]))
np.append(m, np.mean(data[2]))
#m = [np.mean(data[0]), np.mean(data[1]), np.mean(data[2])]

import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


#module to create arrows: http://matplotlib.org/api/patches_api.html
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d(-5, 25)
ax.set_ylim3d(-5, 25)
ax.set_zlim3d(-5, 25)
ax.plot(data[0], data[1], data[2], '.')
a = Arrow3D([9, v_1[0]],
            [11.5, v_1[1]],
            [7.5, v_1[2]],
            mutation_scale=5,
            lw=3,
            arrowstyle="-|>",
            color="r")
b = Arrow3D([9, v_2[0]],
            [11.5, v_2[1]],
            [7.5, v_2[2]],
            mutation_scale=5,
            lw=3,
            arrowstyle="-|>",
            color="r")
c = Arrow3D([9, v_3[0]],
            [11.5, v_3[1]],
            [7.5, v_3[2]],
            mutation_scale=5,
            lw=3,
            arrowstyle="-|>",
            color="r")
ax.add_artist(a)
ax.add_artist(b)
ax.add_artist(c)
plt.show()
'''
a = Arrow3D([m[0], v[0][0]],
            [m[1], v[1][0]],
            [m[2], v[2][0]],
            mutation_scale=20,
            lw=5,
            arrowstyle="-|>",
            color="r")

b = Arrow3D([m[0], (first_v[2]-m[0])],
            [m[1], (sec_v[2]-m[1])],
            [m[2], (third_v[2]-m[2])],
            mutation_scale=20,
            lw=5,
            arrowstyle="-|>",
            color="r")
c = Arrow3D([m[0], (first_v[1]-m[0])],
            [m[1], (sec_v[1]-m[1])],
            [m[2], (third_v[1]-m[2])],
            mutation_scale=20,
            lw=5,
            arrowstyle="-|>",
            color="r")
'''

#ax.add_artist(b)
#ax.add_artist(c)
