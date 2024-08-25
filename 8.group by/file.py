'''if you have random data and you need to do it serially. then we can use group by function which can group similar data. and return new df.'''
import pandas as pd
var1 = pd.DataFrame({"name":["a","b","c","d","a","b","a","b","a","c","c","d"],
                     "subject":[12,13,14,12,13,14,15,23,25,16,10,34],
                     "subject_2":[23,24,25,26,27,28,29,30,25,34,35,56]})

print(var1)


var1_new = var1.groupby("name")  #it will gropu data in name column with same column name.
print(var1_new)
for i, j in var1_new: 
    print(i)
    print(j)
    print()


var1_new.get_group("a") # it will print only grop a

var1_new.min() # we can  find min of each group.

# var1_new.max()
var1_new.mean()

li = list(var1_new)   # we can convert it in to list also
print(li)