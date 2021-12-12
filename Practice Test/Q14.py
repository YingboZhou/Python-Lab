import numpy as np

x = np.array([1,2,3,4,5,6,7])
print("Original array: ", x)

n = 0
for i in x:
    if i % 2 != 0:
        n += 1
print("Number of odd elments in the NumPy array: ", n)

m = 0
for i in x:
    if i % 2 == 0:
        m += 1
print("Number of odd elments in the NumPy array: ", m)