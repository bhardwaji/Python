import numpy as np

# special numpy error

# array filled with zero

x_zero = np.zeros(4)
print(x_zero)

print()

x_zero1 = np.zeros((3, 4))
print(x_zero1)

print(
    """

"""
)

# array filled with 1's
x_ones = np.ones(4)
print(x_ones)
print("\n\n\n")

x_ones = np.ones((4, 5))
print(x_ones)
print("\n\n\n")

# array filled with 1's
x_empty = np.empty(4)
print(x_empty)
print("\n\n\n")


# range array
rangeArray = np.arange(5)
print(rangeArray)
print("\n\n\n")


# array diagonal filled with 1's'
arrayDiagonal = np.eye(3)
print(arrayDiagonal)
print("\n\n\n")

arrayDiagonal = np.eye(3, 5)
print(arrayDiagonal)
print("\n\n\n")

# elements in arrary with space
arrayspace = np.linspace(0, 10, num=5)
print(arrayspace)
arrayspace = np.linspace(0, 20, num=5)
print(arrayspace)
