# Zadanie2
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
#data:
input_file = 'dane.txt'
f = open(input_file, "r")

lines = f.read()
lines_sep = lines.split('\n')
dataX = [float(x) for x in lines_sep[0].split()]
dataY = [float(x) for x in lines_sep[2].split()]
#Plot:
plt.figure()
ax = plt.axes(polar = True)
ax.set_facecolor("grey")
plt.scatter(dataX, dataY, c=dataY, cmap = plt.cm.hsv)
plt.show()


