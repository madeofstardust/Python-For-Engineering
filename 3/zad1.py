#Zad1
'''Create an array of 25 random floating-point numbersin the range [0, 100] and 
set the highest element equal to200 and all numbers smaller than50 equal to 0'''

import numpy as np

a = np.random.uniform(low=0, high = 100, size= 25)
a[a<50] = 0
a[a==np.max(a)] = 200

