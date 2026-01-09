

#integer array indexing
import numpy as np


x = np.array([[1,2,3,4],
              [5,6,4,8],
              [2,10,11,5],
              [31,45,15,160]])
print(np.sort(x))


#slicing

print(x[np.array([1,3,2,0]),1:3])



print(x.dtype)




