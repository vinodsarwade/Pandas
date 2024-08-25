import pandas as pd
df = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\cereal.csv")
print(df)

'''interpolate will autometically replce NaN value from dataframe to a linear values in df.
but now interpolate will not support for latest version so we can use infer_objects insted.
this will only replace for int value. not for string. '''
df.interpolate()
# df.infer_objects()


#suppose we have multiple NaN value in column and you need to replace only 2 value from backword side (down -> up side) then use direction backword.
df.interpolate(limit_direction="forward", limit= 2)
df.interpolate(limit_direction="backward", limit= 2)
df.interpolate(limit_direction="both", limit= 2)  # fill data from both side.