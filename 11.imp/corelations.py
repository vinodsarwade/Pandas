#The corr() method calculates the relationship between each column in your data set.
df.corr()

'''
result:
 Duration     Pulse  Maxpulse  Calories
  Duration  1.000000 -0.155408  0.009403  0.922721
  Pulse    -0.155408  1.000000  0.786535  0.025120
  Maxpulse  0.009403  0.786535  1.000000  0.203814
  Calories  0.922721  0.025120  0.203814  1.000000
'''
#The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
#The number varies from -1 to 1.
'''Perfect Correlation:1.000000 or -1.00000
Good Correlation: 0.9220000  or -0.9220000
BAd Correlation: 0.0099400 or -0.009400 
'''