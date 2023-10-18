import numpy as np

# Random No Generate using Rand() function

arr = np.random.rand(5)
print(arr, "\n")
arr = np.random.rand(2, 5)
print(arr, "\n")

# Random No Generate using Randn() function
arr = np.random.randn(2, 5)
print(arr, "\n")


# Random No Generate using Ranf() function  [0.0 se 1.0 tak )
arr = np.random.ranf(5)
print(arr, "\n")

# Random No Generate using Randint( low, high , totalno) function
arr = np.random.randint(1, 10)
print(arr, "\n")
arr = np.random.randint(1, 10, 5)
print(arr, "\n")
