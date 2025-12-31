import pandas as pd

data = pd.read_csv(r"C:\Users\harsh\Downloads\basic-data.csv")

print(data[["Name","Age"]].head(1))
print(data.iloc[0])
print(data.iloc[0:6])
print(data[data["Age"]==60])