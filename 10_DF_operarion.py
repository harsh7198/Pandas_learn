import pandas as pd

import pandas as pd

data = [
    {"Subject" : "math", "Score" : 9},
    {"Subject" : "science", "Score" : 8},
    {"Subject" : "chemistry", "Score" : 7},
    {"Subject" : "chemistry", "Score" : 6},
    {"Subject" : "chemistry", "Score" : 5},
]

df = pd.DataFrame(data)
print(df.head(1)) # show top(n) rows

print(df.tail(1)) # show tail(n) rows

print(df.info()) # show info like number of rows and column , data types and so on

