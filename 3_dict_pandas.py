import pandas as pd

my_dict ={
    "name" : "Harsh",
    "age" : 19,
    "num" : 24
}

my_series =pd.Series(my_dict)
print(my_series)