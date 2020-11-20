# Ex1
''' 
a) Generate 100 random points sample from a normal distribution 
(mu=3.0, sigma=1.0) and visualize them as a histogram

b) Generate 100 random points sample from a normal distribution 
(mu=1.0, sigma=2.0) and visualize them together with the previous histogram as 
a histogram.

c) Calculate the misclassification rate for these two distributions.

d) Fit a normal distribution function to the first data set.

e)Generate 100 times 100 random points sample from a normal distribution 
(mu=3.0, sigma=1.0). Create a histogram of the means and calculate the standard 
error.

f)Repeat the previous point 1000 times instead of 100. How does the standard 
error differ?
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# a)
mu_1, sigma_1 =  3.0, 1.0
x = np.random.normal(mu_1, sigma_1, 100)

plt.figure()
plt.hist(x, rwidth = 0.5, color = '0.75')
plt.show()

# b)
mu_2, sigma_2 = 1.0, 2.0
y = np.random.normal(mu_2, sigma_2, 100)

plt.figure()
plt.hist([x, y])
plt.show()

# c)

threshold = (sigma_1*mu_2 +sigma_2 + mu_1)

x_below_thres= sum(x < threshold)
y_above_thres= sum(y > threshold)

x_overlap = x_below_thres/ len(x)
y_overlap = y_above_thres/ len(y)

misclassification_rate = (x_overlap + y_overlap) / 2
print(misclassification_rate)

# d)
count, bins, ignored = plt.hist(x, 30, normed=True)
plt.plot(bins, 1/(sigma_1 * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu_1)**2 / (2 * sigma_1**2) ),
          linewidth=2, color='r')
plt.show()

# e)
mu_3, sigma_3 =  3.0, 1.0
means = np.empty(100)
stds = np.empty(100)
for i in range (100):
    x = np.random.normal(mu_3, sigma_3, 100)
    np.append(means, np.mean(x))
    np.append(stds, np.std(x))

colors = ['0.75', '0.35']
plt.figure()
plt.hist([means, stds], rwidth = 0.5, color = colors)
plt.show()

# f)
stds_2 = np.empty(1000)
for i in range (1000):
    x = np.random.normal(mu_3, sigma_3, 100)
    np.append(stds_2, np.std(x))
    




