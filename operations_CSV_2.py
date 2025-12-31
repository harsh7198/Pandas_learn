import pandas as pd

data = pd.read_csv(r"C:\Users\harsh\Downloads\basic-data.csv")

# sort by column

print(data.sort_values(by="Age")) # ascending  order
print(data.sort_values(by="Age", ascending=False)) # descending order
print(data[data["Name"] == "Name_10"])

print(data["Age"].mean())
print(data["Age"].min())
print(data["Age"].max())
print(data.groupby("Age")["Age"].mean())
data.to_csv(r"C:\Users\harsh\Downloads\new_data.csv") # save new file