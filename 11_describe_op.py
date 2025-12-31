import pandas as pd

data = [
    {"Subject" : "math", "Score" : 9},
    {"Subject" : "science", "Score" : 8},
    {"Subject" : "chemistry", "Score" : 7},
    {"Subject" : "chemistry", "Score" : 6},
    {"Subject" : "chemistry", "Score" : 5},
]

df = pd.DataFrame(data)
print(df.describe())