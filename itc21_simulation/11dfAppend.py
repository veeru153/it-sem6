import pandas as pd

df = pd.DataFrame([[1,2], [3,4]], columns=list('AB'))
print("Original Dataframe:")
print(df)

df2 = pd.DataFrame([[5,6],[7,8]], columns=list('AB'))
resDf = df.append(df2)
print("After adding new rows:")
print(resDf)
