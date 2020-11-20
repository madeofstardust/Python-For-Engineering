# PFE 2
#Zad1

import matplotlib.pyplot as plt
x1 = [1, 2, 3, 4]
y1 = [3, 7, 4.5, 8]

x2 = [1, 2, 3, 4]
y2 = [3.5, 4, 6.5, 7]
plt.plot(x1,y1, label = "funkcja 1", linestyle = "dashdot", marker = "o", color = "green")
plt.plot(x2,y2, label = "funkcja 2", linestyle = "dashed", marker = "^", color ="red")

plt.xlim(0.5, 4.5)
plt.xticks([1, 2, 3, 4])

plt.ylim(2.75, 8.25)
plt.yticks([3, 4.5, 7, 8])

plt.legend()
plt.savefig('wykres.png')
plt.show()