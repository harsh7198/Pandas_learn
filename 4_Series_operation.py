import pandas as pd

my_series = pd.Series([ 10 , 20 , 30 , 40 , 50 ], index = ["num1", "num2", "num3", "num4", "num5"])
print (my_series[ 0 ])
print (my_series['num3'])