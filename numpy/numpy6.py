import numpy as np

x = np.array([[12, 3, 4], [1, 2, 3]])
print(x)

for i in x:
    for y in i:
        print(y)

x = np.array([[12, 3, 4], [1, 2, 3]], ndmin=15)
print(x)
