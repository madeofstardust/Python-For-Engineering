# zad5
import matplotlib.pyplot as plt
#data:
input_file = 'dane4.txt'
f = open(input_file, "r")

lines = f.read()
dataX = [float(x) for x in lines.split()]

plt.figure()
plt.subplot(121)
plt.hist(dataX, bins = 30, color='black')
plt.subplot(122)
plt.hist(dataX, bins = 30, color='red', cumulative = True)
plt.show()

