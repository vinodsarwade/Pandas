import pandas as pd 
data = pd.DataFrame({
    "A":[1,2,3,4,5],
    "B":[6,7,8,9,10],
    "C":[11,12,13,14,15],
    "E":[20,21,22,23,24]
})
print(data)


pop = data.pop("B") #for pop we use () with column to be delete
print(pop)

print(data)

del data["E"]   #for delete we use [] with column to be delete