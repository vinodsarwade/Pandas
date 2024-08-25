import pandas as pd
var = pd.DataFrame({"day":[1,2,3,4,5,6], "eng":[10,12,13,14,15,16], "math":[43,22,56,43,66,77]})
print(var)
pd.melt(var)  # using melt we can reshape df in column wise


pd.melt(var, id_vars=["day"])  #by passing id_vars param we can create perticuler column as a id. means this columns are first column in df.

#in above cell we can see all data is stored in variable column and value column. we can change this names also
pd.melt(var, id_vars=["day"], var_name="python", value_name="marks") 

