# Pandas  provides two data structures for processing the data.
#series & DataFrame and panel
 
'''Series: 
        A Pandas Series is like a column in a table
        it is defined as a one-dimensional array that is capable of storing various data types.
'''

import pandas as pd
x = [3,4,5,6,7,8]
var = pd.Series(x)
print(var)
print(type(var))



x = [3,4,5,6]
ser = pd.Series(x)
index = pd.Series(x, index=['a','b','c','d'])      #to change index of table by default it's 0-->n
datatype = pd.Series(x, index=['a','b','c','d'], dtype='float')     #convert to float 
name = pd.Series(x, index=['a','b','c','d'], dtype='float', name ='python')    # give specific name to dataset

print(ser)
print(index)
print(datatype)
print(name)

print(ser[2])        #to get element of array
print(index['b'])   # we can access the elements using index of table



'''using dictionay'''

dic = {"name":['python','c','c++','java'], "por":[12,13,14,15], "rank":[1,4,3,2]}
var1 = pd.Series(dic) 
print(var1)


import pandas as pd
s = pd.Series(12)            # create series of 12 at 0th position 
m = pd.Series(12, index = [1,2,3,4,5,6,7,8]) #create series for 12 at given index position
print(s)
print(m)


#if we need to add two Series data it will add likw below.but it will add up to same
#index which is present in both series. (size should be same ) else it print NaN(not a number)
#in numpy if we did this we got broadcast error. but pandas will support this. 

m = pd.Series(12, index = [1,2,3,4,5,6,7,8])
n = pd.Series(12, index = [1,2,3,4])
print((m + n))