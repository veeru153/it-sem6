import pandas as pd
import numpy as np

arr1 = [1,2,3] 
arr2 = [4,5,6] 
arr3 = [7,8,9] 
arr4 = [10,11,12]
arr = np.array(arr1 + arr2 + arr3 + arr4).reshape(4,3)

df = pd.DataFrame.from_records(arr)
print("DataFrame")
print(df)