# Datatypes in numpy
import numpy as np

var = np.array([1, 2, 3, 4, 5])
print(var.dtype)

var = np.array(["hello"])
print(var.dtype)

var1 = np.random.randint(1, 6, 5)
var2 = np.array([1, 2, "hello"])
print(var1.dtype)
print(var2.dtype)
print()

var = np.array([1, 2, 3, 4, 5], np.int8)
print(var)
print(var.dtype)

var = np.array([1.0, 2, 3, 4, 5], dtype="f")
print(var)
print(var.dtype)

var = np.array([1, 2, 3, 4, 5])
new_one = var.astype(float)
print(var)
print(new_one)
