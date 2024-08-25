import pandas as pd
var = pd.DataFrame({"day":[1,2,3,4,5,6], 
                    "name":["a","b","c","a","b","c"],
                    "eng":[10,12,13,14,15,16], 
                    "math":[43,22,56,43,66,77]})
print(var)

var.pivot(index="day",columns="name")

var.pivot(index="day",columns="name", values="eng") #by passing values we can get perticuler pivot table column.

var.pivot_table(index="name", columns="day", aggfunc="sum", margins=True)  #by passing aggfunc we can calculate sum, min, max, mean data from df
                                                                   # by passing margins, it will return sum of each row in a table.

