'''
    Duration          Date  Pulse  Maxpulse  Calories
  0         60  '2020/12/01'    110       130     409.1
  1         60  '2020/12/02'    117       145     479.0
  2         60  '2020/12/03'    103       135     340.0
  3         45  '2020/12/04'    109       175     282.4
  4         45  '2020/12/05'    117       148     406.0
  5         60  '2020/12/06'    102       127     300.0
  6         60  '2020/12/07'    110       136     374.0
  7        450  '2020/12/08'    104       134     253.3
  8         30  '2020/12/09'    109       133     195.1
  9         60  '2020/12/10'     98       124     269.0
  10        60  '2020/12/11'    103       147     329.3
'''
#in above df in Duration column all value between 45-60 but at row 7 it is 450 which is wrong.
#so we can directly replace perticular value using loc
df.loc[7, 'Duration'] = 45



'''For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.
Example
Loop through all values in the "Duration" column.
If the value is higher than 120, set it to 120:'''

for x in df.index:
  if df.loc[x, "Duration"] > 120:  #in above case 450 data at 7th row is bigger than 120 so it will replace by 120
    df.loc[x, "Duration"] = 120


#Delete rows where "Duration" is higher than 120:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)