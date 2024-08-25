import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4], "B":[10,11,12,13]})
var2 = pd.DataFrame({"A":[1,2,3,4], "C":[20,21,22,23]})

pd.merge(var1, var2, on ="A")  # for merging we need to give 1 parameter which is common in both df.
                               #here A column is same for both df.


import pandas as pd
num1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})
num2 = pd.DataFrame({"A":[1,2,3,5], "C":[21,22,23,24]})

pd.merge(num1, num2, on="A") #here in num2 i changed 4 to 5 in "A". so now this column are not same.so it will merge up to 3 only


#if you want print whole df after changing element or you have missing value then we can pass how="" parameter.
# pd.merge(num1, num2, how="left") #it will check & merge from left side i.e. in num1 "A", and missing element in right side ie."C" printed as NaN
# pd.merge(num1, num2, how="right") #it will check & merge from right side i.e. in num2 "A", and missing element in left side ie."B" printed as NaN

pd.merge(num1, num2, how="outer") #it will print both side of data with missing values.

pd.merge(num1, num2, how="outer", indicator=True) #by passing indicator you check on which side data is present or not.


import pandas as pd
num3 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})
num4 = pd.DataFrame({"A":[1,2,3,5], "B":[21,22,23,24]})

pd.merge(num3, num4, left_index=True, right_index=True) # if you have same column name but diff data. to print this type of data pass left_index and right_index in param.
                     #then only we can print same column name data.