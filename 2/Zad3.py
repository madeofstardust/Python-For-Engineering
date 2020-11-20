# Zad3
import matplotlib.pyplot as plt
#data:
input_file = 'dane2.txt'
f = open(input_file, "r")

lines = f.read()
lines_sep = lines.split('\n')
dataX = [float(x) for x in lines_sep[0].split()]
dataY = [float(x) for x in lines_sep[1].split()]

plt.figure()

plt.xlim(0, 12)
plt.xticks([0,2,4,6,8,10,12])

plt.ylim(0.00,1.00)
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])

colors = plt.cm.YlGnBu(dataY)

plt.bar(dataX, dataY, width = 0.8, align = 'edge', color=colors, ec="k")
plt.show()
