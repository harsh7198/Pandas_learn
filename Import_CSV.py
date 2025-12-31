import pandas as pd

data = pd.read_csv(r"C:\Users\harsh\Downloads\basic-data.csv")
print(data.head()) # show first 5 rows by default
print(data.tail())
print(data.shape)
print(data.columns)
print(data.dtypes)
print(data.info)
print(data.describe())