import pandas as pd
dic = {"a":[1,2,3,4,5], "b":[1,2,3,4,5],"c":[1,2,3,4,5]}
frame = pd.DataFrame(dic)
print(frame)

frame.to_csv("Test.csv") #create csv file named Test.csv
frame.to_csv("Test_new.csv", index = False) #remove index
frame.to_csv("Test_new1.csv", index= False, header=[1,2,3]) #rename column name using header


                     ##  read csv file  ##

import pandas as pd 
read_csv = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Test_new.csv")
print(read_csv)

read_csv = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Test_new.csv",nrows=2)  # to get no of rows then use 'nrows'
print(read_csv)

read_csv_1 = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Student.csv", usecols=["Age"])  # to get perticuler column in csv file use "usecols=["column_name"]"
print(read_csv_1)

read_csv_2 = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Student.csv", usecols=[2])  # to get perticuler column in csv file we can give interger position of column also.
print(read_csv_2)

read_csv_3 = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Student.csv", skiprows=[0])  #using this we can skip rows in a csv file
print(read_csv_3)

read_csv_4 = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Student.csv",index_col=["Age"])  #using this we can use Age column as a index in a file .rather than using original index.
print(read_csv_4)

read_csv_5 = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Student.csv",header=2)  #using this we can use second column as a header in a file.
print(read_csv_5)

read_csv_6 = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Student.csv",names=["col1","col2","col3","col4","col5"])  #can give header names in a file 
print(read_csv_6)

read_csv_7 = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Student.csv", dtype={"Age":"float"}) #convert age column to float
print(read_csv_7)






import pandas as pd 
dic = {"A":[1,2,3], "B":[4,5,6], "C":[7,8,9]}
df = pd.DataFrame(dic, index=["a", "b", "c"])
print(df)
print(df.loc["b"])   # using loc we can access rows using given index./ if not  index changed then we can give integer position also
print(df.iloc[2])  # using iloc we can access rows using integer position.

csv = df.to_csv("practice.csv", index=False) 
read = pd.read_csv("practice.csv")
print(read)