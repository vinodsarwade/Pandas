import pandas as pd
csv = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Student.csv")
print(csv)

csv.index #start and stop index

csv.columns #colums names

csv.describe() #gives function to int value only

csv.head(2) #get first 2 rows , bydefault gives 5 rows

csv.tail() #get last 2 rows , bydefault gives 5 rows

csv[1:6] #slicing to get specific data

csv[12:5:-1] #revrese

csv.index.array  # convert index to array

import numpy as np
# csv.to_numpy  # convert dataframe to numpy array
v = np.asarray(csv)
print(v)

csv.sort_index(ascending=False,axis=0) #sort data in decending order at axis 0

csv.loc[0,"Gender"] = "Male/Female"  #change specific element in dataframe,,,  loc[row, column]="changes"
print(csv)

csv.loc[[4,5],["Age","Gender"]] #get rows and columns only

csv.loc[[5, 6]]  #get full rows

csv.iloc[0, 2]  #to get perticulat element give rows number and column number

csv.drop("Ethnicity",axis=1) #drop column