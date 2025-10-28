import numpy as np
import pandas as pd
import numpy.random as randn

# one dimensional array
array_1d = np.array([1, 2, 3, 4, 5, 6])
print(array_1d)

# two dimensional array (2x2 matrix)
matrix_1 = np.array([[1, 2, 3], [3, 4, 5]])
print(matrix_1)

matrix_2 = np.array([[6, 5, 4], [3, 2, 1]])

print(matrix_2*matrix_1)  # thats only element wise multiplication

#real matrix multiplication
print(np.dot(matrix_1, matrix_2.T))

