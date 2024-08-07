import pandas as pd
list1 = [1,2,3,4,5,6]
var = pd.DataFrame(list1)
print(var)
print(type(var))



dictionary = {"a":[1,2,3,14,5], "s":[1,2,3,4,5],"d":[1,2,3,4,5],1:[1,2,3,4,5]}
var1 = pd.DataFrame(dictionary)

print(var1)
print(var1["a"][3])  #get specific element from DataFrame
var2 = pd.DataFrame(dictionary, columns=["a"]) #print only column a 
print(var2)


list_1 = [ [1,2,3,4,5], [11,12,13,14,15] ]
v = pd.DataFrame(list_1)
print(v)


sr = {
    "s":pd.Series([1,2,3,4]), 
    "r":pd.Series([5,6,7,8])}
n = pd.DataFrame(sr)
print(n)


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)

print(myvar)

print(myvar.loc[0])     # to get rows from DataFrame use loc[] function, it will return a Series
print(myvar.loc[[0,1]])    # to get multiple rows then use list of rows in loc[] it will return a DataFra  