import pandas as pd
import numpy as np

my_series =pd.Series([10,20,30,40,50])
print(np.min(my_series)) # min
print(np.max(my_series)) # max
print(np.mean(my_series)) # mean (average)
print(np.median(my_series)) # median
print(my_series.dtype)