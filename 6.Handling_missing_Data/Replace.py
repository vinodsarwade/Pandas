import pandas as pd
df  = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\cereal.csv")
print(df)

df.replace(to_replace="C",value="O+")   #using this we can replace all values of "C" to "O+" in whole dataframe.
df. replace({"name":'[A - Z]'}, 22, regex=True)  #using dict we can replace [A - Z] letters from column name to 22, using regular expression.

df.replace(1, method="bfill")   #using this all 1 in df replaced by backward fill in whole df
                                # we can use ffill for forward replace

# df.replace(1, method="bfill",limit=2) #by passing limit we can replace data up to seted limit. not whole df.