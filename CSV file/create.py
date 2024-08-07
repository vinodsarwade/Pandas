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


read_csv = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Test_new.csv",nrows=1)  # to get no of rows then use 'nrows'
print(read_csv)




import pandas as pd 
dic = {"A":[1,2,3], "B":[4,5,6], "C":[7,8,9]}
df = pd.DataFrame(dic, index=["a", "b", "c"])
print(df)
print(df.loc["b"])   # using loc we can access rows using given index./ if not  index changed then we can give integer position also
print(df.iloc[2])  # using iloc we can access rows using integer position.

csv = df.to_csv("practice.csv", index=False) 
read = pd.read_csv("practice.csv")
print(read)