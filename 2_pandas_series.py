import pandas as pd 
# pandas series is like an column , one type of 1D , hold data of any type 
harsh = [1,2,3]
sharadnew = pd.Series(harsh)
print(sharadnew)
s = pd.Series([10,20,30,40,50] , index = ["A", "B", "C", "D", "E"])
print(s)

