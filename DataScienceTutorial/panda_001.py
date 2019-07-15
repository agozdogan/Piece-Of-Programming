import matplotlib.pyplot as plt
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns  # visualization tool

data = pd.read_csv("DataScienceTutorial\pokemon.csv")
#print(data.corr())

""" data.Speed.plot(kind = 'line', color = 'g',label = 'Speed',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
data.Defense.plot(color = 'r',label = 'Defense',linewidth=1, alpha = 0.5,grid = True,linestyle = '-.')
plt.legend(loc='upper right')     # legend = puts label into plot
plt.xlabel('x axis')              # label = name of label
plt.ylabel('y axis')
plt.title('Line Plot')            # title = title of plot
plt.show() """

# x = data['Defense']>200
# print(data[x])

# print(data.head())

# print(data['Type 1'].value_counts(dropna = False))

data.boxplot(column='Attack', by='Legendary')
plt.show()

i = 0 
while i!= 5 : 
    print ( 'i is :', i)
    i += 1 
print(i, "is equal to 5")    

dic = {"spain":"madrid", "spain":"barcelona","portugal":"lisbon"}
for key,value in dic.items():
    print(key, ':', value)

liste = [1,2,3,4,5]

for i in liste:
    print('i is :', i)