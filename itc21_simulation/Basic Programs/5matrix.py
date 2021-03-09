import pandas as pd
import numpy as np
import random

v = np.random.randint(10, size=16)
col_names = ["col_1", "col_2", "col_3", "col_4"]
row_names = ["row_1", "row_2", "row_3", "row_4"]

d = pd.DataFrame(v.reshape(len(row_names), len(col_names)), index=row_names, columns=col_names)
print(d)

print("\n")