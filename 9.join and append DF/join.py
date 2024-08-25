import pandas as pd
df = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,13]})
df2 = pd.DataFrame({"C":[10,20], "D":[11,22]})
df.join(df2)  # we can add how param as well to print specific data


df = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,13]})
df2 = pd.DataFrame({"C":[10,20], "B":[11,22]})     
# df.join(df2)     # due to same column name used for B it will raise an error .. to fix that we can use 'suffix' param
df.join(df2, lsuffix="_12", rsuffix="_12") #left suffix and right