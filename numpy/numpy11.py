import numpy as np

"""airthamtic functions"""
var = np.random.randint(1, 6, 5)
print(var)
print(np.min(var))
print("position in array is", np.argmin(var))  # position min

print()
print(np.max(var))
print("position in array is", np.argmax(var))  # position max

var = np.array([[1, 2, 4], [5, 6, 7]])
"""we need to put axis =0 (row)or axix =1(column) in 2d array min value in perticular axis"""
print()
print(var)
print("\n", np.min(var, axis=0))
print(np.min(var, axis=1))

"""squareroot"""
print("\n var is \n", var)
print("\n \n square root is \n\n ", np.sqrt(var))
"""cuberoot"""
print("\n \n cube root is \n\n ", np.cbrt(var))


"""sin and cos values"""
print()
var = np.array([1, 0.5, 3 / 2])
print("sin values", np.sin(var))
print("cos values", np.cos(var))

"""np.cumsum(x)"""

var = np.array([1, 2, 4])
"""it will add value with previous value and print"""
print(np.cumsum(var))
