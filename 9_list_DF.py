import pandas as pd

data = [
    {"Subject" : "math", "Score" : 9},
    {"Subject" : "science", "Score" : 8},
    {"Subject" : "chemistry", "Score" : 7},
    {"Subject" : "chemistry", "Score" : 6},
    {"Subject" : "chemistry", "Score" : 5},
]

df = pd.DataFrame(data)
print(df)

data1 = [
    {"Subject" : "math", "Score" : 9},
    {"Subject" : "science", "Score" : 8},
    {"Subject" : "chemistry", "Score" : 7},
    {"Score" : 6}, # print NAN value
    {"Subject" : "chemistry", "Score" : 5},
]

df2 = pd.DataFrame(data1)
print(df2)
