import pandas as pd
dic = {"a":[1,2,3,4,5], "b":[1,2,3,4,5],"c":[1,2,3,4,5]}
frame = pd.DataFrame(dic)
print(frame)

frame.to_csv("Test.csv") #create csv file named Test.csv
frame.to_csv("Test_new.csv", index = False) #remove index
frame.to_csv("Test_new1.csv", index= False, header=[1,2,3]) #rename column name using header


## read csv file

import pandas as pd 
read_csv = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Test_new.csv")
print(read_csv)


read_csv = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Test_new.csv",nrows=1)  # to get no of rows then use 'nrows'
print(read_csv)
