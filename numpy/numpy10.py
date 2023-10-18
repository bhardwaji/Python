"""Airthmatic Operations In arrarys """
import numpy as np


""" using operators in One Dimension array"""
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])

# add = a + 5
# print(add)


# add = a + b
# print(add)
# sub = a - b
# print(sub)
# mul = a * b
# print(mul)
# div = a / b
# print(div)
# mod = a % b
# print(mod)
# coficient = a // b
# print(coficient)
# exponent = a**b
# print(exponent)


"""Airthmatic Operations On 2d Array """

addition = np.add(a, b)
print(addition)
addition = np.add(a, 4)
print(addition)
# same functions like
# np.add(a,b)
# np.subtract(a,b)
# np.multiply(a,b)
# np.divide(a,b)
# np.mod(a,b)
# np.power(a,b)
# np.reciprocal(a)   i.e.  1/a
var = np.array([2, 4, 6, 8, 9])
reci = np.reciprocal(var)
print(reci)
var = np.array([1, 2, 3, 4, 5], dtype=float)
reci = np.reciprocal(var)
print(reci)


var1 = np.array([[1, 2, 3], [10, 11, 12]])
var2 = np.array([[4, 5, 6], [7, 8, 9]])
print("var1\n", var1)
print("var 2 \n", var2)
addition = var1 + var2
substraction = var1 - var2
print("addition \n", addition)
print("substraction \n", substraction)
"""helpful in matrix """
