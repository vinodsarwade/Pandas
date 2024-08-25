import pandas as pd
sr1 = pd.Series([1,2,3,4])
sr2 = pd.Series([11,12,13,13])
pd.concat([sr1, sr2])


p1 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})
p2= pd.DataFrame({"A":[1,2,3,5], "B":[21,22,23,24]})
pd.concat([p1, p2]) # we can pass axix = 1 for colums wise concat


p3 = pd.DataFrame({"A":[1,2,3,4], "B":[11,12,13,14]})
p4= pd.DataFrame({"A":[1,2], "B":[21,22]})
# pd.concat([p3, p4], axis=1) # in this case we dont have equal data in both df. if we want to print only available data without using NaN value use join param
pd.concat([p3, p4],axis=1, join="inner") # print only data thode present in both df. (intersection)

