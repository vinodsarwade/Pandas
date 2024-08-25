#Pandas uses the plot() method to create diagrams.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.plot()
plt.show()



#if we want to plot perticular graph then use kind param with name of graph , and x and y are axis names on the graph

df = pd.read_csv('data.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()



#A histogram needs only one column.
#A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?
df["Duration"].plot(kind = 'hist')
plt.show()