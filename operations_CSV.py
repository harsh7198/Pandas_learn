import pandas as pd

data = pd.read_csv(r"C:\Users\harsh\Downloads\basic-data.csv")

print(data[["Name","Age"]].head(1))
print(data.iloc[0]) # print entire rows
print(data.iloc[0:18])
print(data[data["Age"]==60])

# check for missing value (NULL)

print(data.isnull().sum()) # give total of missing data in csv file
print(data.dropna()) # remove missing value
print(data.fillna(0)) # fill mising value