# types of array
# one dimension array
# 2D Array
# 3D array
# High Dimension Array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.ndim)
print(arr)
arr = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print(arr.ndim)
print(arr)
arr = np.array([[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 2, 4]]])
print(arr.ndim)
print(arr)
arr = np.array([[[[[[[[[1, 2, 3, 4, 5]]]]]]]]])
print(arr.ndim)
print(arr)


arr = np.array([1, 2, 3, 4], ndmin=32)
print(arr.ndim)
print(arr)
