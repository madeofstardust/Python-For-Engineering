# Zad4
import matplotlib.pyplot as plt
#data:
input_file = 'dane3.txt'
f = open(input_file, "r")

lines = f.read()
dataX = [float(x) for x in lines.split()]
dataX.sort()
plt.figure()
plt.pie(dataX, wedgeprops={"edgecolor":"0",'linewidth': 0.5})
plt.show()
