import pandas as pd
var = pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
print(var)



import pandas as pd 
var = pd.DataFrame(
    {
        "A":[1,2,3,4], "B":[5,6,7,8]
    })
print(var)

var["C"] = var["A"] + var["B"]    #addition of both column
print(var)

var["D"] = var["A"] - var["B"]    #substraction of both column
print(var)

var1 = pd.DataFrame({"A":[10,20,30,40], "B":[50,60,70,80]})
print(var1)


var1["python"] = var1["A"] <= 20     #create new column named as "python" and check if data in column "A" is less than 20
print(var1)

var1["python_1"] = var1["B"] >= 60     #create new column named as "python_1" and check if data in column "B" is greater than 60
print(var1)
