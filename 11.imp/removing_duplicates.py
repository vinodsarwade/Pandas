'''
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
  11        60  '2020/12/12'    100       120     250.7
  12        60  '2020/12/12'    100       120     250.7
  13        60  '2020/12/13'    106       128     345.3
  14        60  '2020/12/14'    104       132     379.3
  15        60  '2020/12/15'     98       123     275.0
'''

'''By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.
To discover duplicates, we can use the duplicated() method.
The duplicated() method returns a Boolean values for each row:
ExampleGet your own Python Server
Returns True for every row that is a duplicate, otherwise False:'''

print(df.duplicated())


'''To remove duplicates, use the drop_duplicates() method.
Example
Remove all duplicates:'''

df.drop_duplicates(inplace = True)