#zad2
'''Create a matrix 9x9 of random numbers (int32)in the range of -100 to 100.
 Using this matrix create an array that only contains the even elements sorted 
 in ascending order.'''
 
import numpy as np
 
a = np.random.uniform(low = -100, high = 100, size = 81).reshape((9,9))
a.dtype = np.int32

b = a[a%2==0]
b.sort()

