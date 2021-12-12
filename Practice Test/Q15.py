import numpy as np

matrix = np.zeros((7,7))

index = 0
for i in range(7):
    matrix[i][index] = 1
    index += 1
print(matrix)