import numpy as np

matrix = np.array([
    ["r1c1", "r1c2", "r1c3", "r1c4"],
    ["r2c1", "r2c2", "r2c3", "r2c4"],
    ["r3c1", "r3c2", "r3c3", "r3c4"],
    ["r4c1", "r4c2", "r4c3", "r4c4"],
])

print("Original Matrix:")
print(matrix)
print(f"Element at 3rd Column and 2nd Row: {matrix[1][2]}")
print(f"3rd Row: {matrix[2, :]}")
print(f"4th Column: {matrix[:, 3]}")

