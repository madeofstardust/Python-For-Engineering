'''
Implement the activator inhibitor model in python. 
Use a uniform grid size of 100, dx = 0.02, dt= 0.001, T = 15, a = 6, Dv= 5e-3. 
Visualize using matplotlib all 9 patterns of stripes and spots discussed in the 
lecture. Visualize in an image plot 9 consecutive time steps for a selected 
pattern.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

dx = 0.02
dt = 0.001
T = 15
a = 6
Dv = 5*np.exp(-3)
'''
"""
From Ipython cookbook:
"""

import numpy as np
import matplotlib.pyplot as plt
dU = 2.8e-4
dV = 5e-3
a = 6
k = -0.005

size = 100  
dx = 0.02

T = 15 # total time
dt = 0.001  # time step
n = int(T / dt)  # number of iterations

U = np.random.rand(size, size)
V = np.random.rand(size,  size)

def laplacian(Z):
    Ztop = Z[0:-2, 1:-1]
    Zleft = Z[1:-1, 0:-2]
    Zbottom = Z[2:, 1:-1]
    Zright = Z[1:-1, 2:]
    Zcenter = Z[1:-1, 1:-1]
    return (Ztop + Zleft + Zbottom + Zright -
            4 * Zcenter) / dx**2
            
def show_patterns(U, ax=None):
    ax.imshow(U, cmap=plt.cm.copper,
              interpolation='bilinear',
              extent=[-1, 1, -1, 1])
    ax.set_axis_off()
    
    
fig, axes = plt.subplots(3, 3, figsize=(8, 8))
step_plot = n // 9
# We simulate the PDE with the finite difference
# method.
for i in range(n):
    # We compute the Laplacian of u and v.
    deltaU = laplacian(U)
    deltaV = laplacian(V)
    # We take the values of u and v inside the grid.
    Uc = U[1:-1, 1:-1]
    Vc = V[1:-1, 1:-1]
    # We update the variables.
    U[1:-1, 1:-1], V[1:-1, 1:-1] = \
        Uc + dt * (dU * deltaU + Uc - Uc**3 - Vc + k),\
        Vc + dt * (dV * deltaV + Uc - Vc) * a
    # Neumann conditions: derivatives at the edges
    # are null.
    for Z in (U, V):
        Z[0, :] = Z[1, :]
        Z[-1, :] = Z[-2, :]
        Z[:, 0] = Z[:, 1]
        Z[:, -1] = Z[:, -2]

    # We plot the state of the system at
    # 9 different times.
    if i % step_plot == 0 and i < 9 * step_plot:
        ax = axes.flat[i // step_plot]
        show_patterns(U, ax=ax)
        ax.set_title(f'$t={i * dt:.2f}$')