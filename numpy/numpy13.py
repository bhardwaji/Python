import numpy as np

"""broadcasting"""
"""wrong coz elements are not same"""
# var1 = np.array([1, 2, 3, 4])
# var2 = np.array([1, 2, 3, 4, 5])
# print(var1 + var2)
"""error throw"""

"elements are same it can be added"
var1 = np.array([1, 2, 3, 4])
var2 = np.array([1, 2, 3, 4])
print(var1 + var2)

"""
requirements 
same dimensions should be there
atleast one should be bothin column 
atleast 1 should be in both 
"""
var1 = np.array([[23, 34, 45]])
print(var1.shape)
var2 = np.array([[1], [12], [12]])
print(var2.shape)

print("\n var1 \n", var1, "\n var2 \n", var2, "\n")
print(var1 + var2)


"""error : not filleing requirement"""
var2 = np.array([[1], [12], [12]])
print(var1.shape)
var2 = np.array([[1], [12], [12], [15]])
print(var2.shape)

print("\n var1 \n", var1, "\n var2 \n", var2, "\n")
print(var1 + var2)
