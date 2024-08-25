import pandas as pd
csv = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\data.csv")
print(csv)
# print(csv.to_string())  # to_string()   for print whole dataset


'''One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.'''

new_csv = csv.dropna()
print(new_csv)         #dropna return new dataframe , if u want to change original dataframe, use "inplace = True"

new_csv1 = csv.dropna(inplace=True) # can give axis also 0 or 1
print(new_csv1)

new_csv2 = csv.dropna(subset=["Calories"]) #it will drop NaN value from Calories column. 
print(new_csv2)

new_csv3 = csv.dropna(thresh= 1) # we can change value
print(new_csv3)     # the column which has only one NaN value they can thresh/drop. if 2 then thresh 2 NaN value column.
 