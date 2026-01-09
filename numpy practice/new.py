import numpy as np
print(np.zeros((2,3, 2)))

print(np.ones((2,4,2)))


#random method with default_rng will print random values between 0 and 1

from numpy.random import default_rng
print(default_rng(42).random((2,3,2)))