from asyncio.windows_events import NULL

import pandas as pd
import numpy as np

my_array = np.array([1,2,3,4,5,6])
my_series = pd.Series(my_array, index=['a','b','c','d','e','f'])
print(my_series)