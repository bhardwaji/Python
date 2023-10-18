import numpy as np

"""sHAPE KA USE """
arr = np.array([1, 2, 3, 4])
print(arr.shape)
arr = np.array([[1, 2, 3, 4], [1, 3, 56, 7763]])
print(arr.shape)
mul_dim_array = np.array([1, 2, 3, 4, 5], ndmin=4)
print(mul_dim_array.shape)


"""Reshape"""
aar = np.array([1, 12, 3, 4, 5, 6, 6, 7], ndmin=12)
re_arr = aar.reshape(2, 4)
print(re_arr)
print(aar.ndim)
print(re_arr.ndim)

"""convert it into one d"""
_3d = np.array([[[[1, 2, 3], [12, 34, 56], [23, 4, 5], [12, 34, 445]]]])
_oned = _3d.reshape(-1)
print(_oned)
_3d_again = _oned.reshape(3, 4)
print(_3d_again)
