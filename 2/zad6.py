# Zad6
import matplotlib.pyplot as plt
#data:
input_file = 'dane5.txt'
f = open(input_file, "r")

lines = f.read()
boxes = lines.split()

box_1 = [float(x) for x in boxes[0].split(',')]
box_2 = [float(x) for x in boxes[1].split(',')]
box_3 = [float(x) for x in boxes[2].split(',')]

plt.figure(thisPlot)
plt.boxplot((box_1, box_2, box_3))
plt.Axes.set_aspect(thisPlot, aspect=16/9)
plt.show()




