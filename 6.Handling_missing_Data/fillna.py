#fillna
import pandas as pd
fill = pd.read_csv("C:\\Users\\VSARWADE\\Desktop\\Pandas\\Student.csv")
print(fill)

var = fill.fillna("Vinod") # fill  entire NaN value in dataframe by 'Vinod'
print(var)

var2 = fill.fillna({"StudentID":"python", "Ethnicity":"Java", "ParentalEducation":"pandas"}) #likewise we can replace NaN value in perticular column with perticular name.
# print(var2)
fill["StudentID"].fillna(130, inplace = True) #to change value for StudentID column only with 130


fill.fillna(method="ffill") #forward fill,  next element added at NaN value.
fill.fillna(method="bfill")#backward fill,previous element added at NaN value 