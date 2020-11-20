import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch


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



#3D plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d(-5, 25)
ax.set_ylim3d(-5, 25)
ax.set_zlim3d(-5,25)
#example arrow from (0,0,0) to (1,1,1)
a = Arrow3D([9.0, -0.7], [11.5, -0.7], [8.5, -0.2], mutation_scale=20, lw=5, arrowstyle="-|>", color="r")
ax.add_artist(a)


plt.show()