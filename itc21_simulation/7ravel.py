import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(f"Before raveling:");
print(matrix)

arr = np.ravel(matrix);
print(f"After raveling: {arr}")