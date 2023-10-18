import numpy as np

l = []
for i in range(5):
    value = input("enter element")
    l.append(value)
print(l)
print(type(l))
m = np.array(l)
print(m)
print(type(m))
print(m.ndim)
