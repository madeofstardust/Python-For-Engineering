# Difusion models:

'''
1) Bass Difusion Model-  It consists of a simple differential equation that 
describes the process of how new products get adopted in a population. The 
model presents a rationale of how current adopters and potential adopters of a 
new product interact. (Source: wikipedia)

2) Genetics - analyzing a degenerate diffusion equation with singular boundary
    lets the scientists to model the evolution of a polygenic trait under 
    selection and drift. 
    (https://www.sciencedirect.com/science/article/pii/S0022039605003682)

3) Psychology - Stochastic diffusion models can be used to analyze response 
    time data from binary decision tasks. They provide detailed information about 
    cognitive processes underlying the performance in such tasks. Most importantly, 
    different parameters are estimated from the response time distributions of correct 
    responses and errors that map:
        (1) the speed of information uptake, 
        (2) the amount of information used to make a decision, 
        (3) possible decision biases, and 
        (4) the duration of nondecisional processes
    (https://www.ncbi.nlm.nih.gov/pubmed/23895923)
    
4) Medicine - The model addresses both the adoption and the changing extent of 
    use of an evolving, product-based technology and also endogenously accounts 
    for changes in actual and perceived performance. 
    (https://www.sciencedirect.com/science/article/pii/0040162587900114)
    
5) Sociology - most of the evidence produced in sociology and demography to 
    distinguish between explanations based on diffusion arguments from those 
    attributing the primary role to socioeconomic or structural changes is 
    carved out of aggregate, not individual, data. Because the individual 
    adoption process is never defined, the aggregate process is also ill 
    conditioned: there is rarely a way to determine what kind of aggregate 
    evidence one would expect when the individual adoption process is left 
    unspecified.
    (https://www.ncbi.nlm.nih.gov/books/NBK223857/)
'''
# I did not manage to count it by mesyelf, but I have found a pretty cool programm
# which visualises diffusion model; here I modified it a little bit.
# Source: https://scipython.com/blog/a-very-simple-2-d-diffusion-model/
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import  colors

# (Square) grid side length.
m = 40
# Maximum numbter of iterations.
nitmax = 150
# Number of particles in the simulation.
nparticles = 50000
# Output a frame (plot image) every nevery iterations.
nevery = 5
# Constant maximum value of z-axis value for plots.
zmax = 500

# Create the 3D figure object.
# We'll need a meshgrid to plot the surface: this is X, Y.
x = y = np.linspace(1,m,m)
X, Y = np.meshgrid(x, y)

# Initialize the location of all the particles to the centre of the grid.
locs = np.ones((nparticles, 2), dtype=int) * m//2

# Iterate for nitmax cycles.
for j in range(nitmax):
    # Update the particles' locations at random. Particles move at random to
    # an adjacent grid cell. We're going to be pretty relaxed about the ~11%
    # probability that a particle doesn't move at all (displacement of (0,0)).
    locs += np.random.randint(-1, 2, locs.shape)
    if not (j+1) % nevery:
        # Create an updated grid and plot it.
        grid = np.zeros((m, m))
        for i in range(nparticles):
            x, y = locs[i]
            # Add a particle to the grid if it is actually on the grid!
            if 0 <= x < m and 0 <= y < m:
                grid[x, y] += 1
        print(j+1,'/',nitmax)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        # Now clear the Axes of any previous plot and make a new surface plot.
        ax.plot_surface(X, Y, grid, rstride=1, cstride=1, cmap=plt.cm.autumn,
                        linewidth=1)
        ax.set_zlim(0, zmax)    
        plt.show()
        
    