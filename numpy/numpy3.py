import numpy as np

arr = []
for i in range(5):
    arr_value = input("Enter Value to Array : \n")
    arr.append(arr_value)
print(arr)
print(type(arr))
x = np.array(arr)
print(x)
print(type(x))
