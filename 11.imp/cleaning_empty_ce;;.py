import pandas as pd
df = pd.read_csv('data.csv')
df["Calories"].fillna(130, inplace = True)

'''Replace Using Mean, Median, or Mode
A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:'''


df = pd.read_csv('data.csv')
x = df["Calories"].mean() #the average value (the sum of all values divided by number of values).
df["Calories"].fillna(x, inplace = True)

df = pd.read_csv('data.csv')
x = df["Calories"].median()  #the value in the middle, after you have sorted all values ascending.
df["Calories"].fillna(x, inplace = True)


df = pd.read_csv('data.csv')
x = df["Calories"].mode()[0] #the value that appears most frequently.
df["Calories"].fillna(x, inplace = True)