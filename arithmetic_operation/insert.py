import pandas as pd 
var = pd.DataFrame({
    "A":[1,2,3,4,5],
    "B":[6,7,8,9,10]
})
print(var)



var.insert(1,"python", [11,12,13,14,15])  #insert given data at 1th position in dataframe with column name as python.
print(var)

var["python_1"] = var["A"][0:3]    #copy 0 to 3 data from column "A" and  add in a python-1 column.
print(var)