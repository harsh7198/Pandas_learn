import pandas as pd
from win32con import NULL

data = [[1,"Harsh", 19 ], [2,"Rudra", 18]]

df = pd.DataFrame(data, columns=["No.", "Name", "Age"])

print(df)

# dataframe using dictionaries
import pandas as pd
scores ={ 'Subject':["Mathematics", "History", "English", "Science", "Arts"],
'Score':[10,20,30,40,50 ]
}
my_df = pd.DataFrame(scores)
print(my_df)