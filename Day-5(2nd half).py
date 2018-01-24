import matplotlib.pyplot as plt

l=[120,360,458,700,168,425]
plt.hist(l)

plt.show()

import numpy as np
pop=np.random.rand(6)
plt.hist(pop,bins=5)
plt.hist(pop,color='green')
plt.hist(pop,orientation='horizontal')
plt.xscale('log')
plt.hist(pop)
plt.yticks([0.15,2.75])
plt.xticks([0.25,3.75])


#Batch process all the following three lines
h=[10,20,30,40,50]
plt.hist(h)
plt.yticks([0.0,0.4,0.6,0.8,1.0])

#plt.yticks([0.0,0.4,0.6,0.8,1.0,1.5])

plt.xticks([0,5,10,15,20,25,30,35,40,45,50])

plt.xlabel("Value of H")
plt.ylabel("Value of Y")
plt.title("H vs Y")
plt.legend(['blue'])


#For pie chart
labels='Python','C++','Ruby','Java'
sizes=[310,30,145,110]
colors=['gold','yellowgreen','lightcoral','lightskyblue']
explode=(0,0.1,0,0)

plt.pie(sizes,explode=explode,labels=labels,colors=colors,
        autopct='%1.1f%%',shadow=True,startangle=30)

#to rotate the graph
plt.pie(sizes,explode=explode,labels=labels,colors=colors,
        autopct='%22.21f%%',shadow=True,startangle=145)

#Scatter plot
x=np.random.rand(5)
y=np.random.rand(5)
plt.scatter(x,y)

#size of the dot
x=np.random.rand(5)
y=np.random.rand(5)
s1=[10,20,30,40,50]
plt.scatter(x,y,s=s1)


#color of the dot
x=np.random.rand(5)
y=np.random.rand(5)
s1=[10,20,30,40,50]
c1=np.random.rand(5)
plt.scatter(x,y,s=s1,c=c1)


#Bar chart
x=np.arange(4)#Gives an array of specified no of elements
money=[10,20,30,40]
a,b,c,d=plt.bar(x,money)
a.set_facecolor('r')
b.set_facecolor('g')
c.set_facecolor('b')
d.set_facecolor('black')
plt.xticks(x,("A","B","C","D"))
plt.show()

#Just paractice , ignore it
x=np.arange(4)#Gives an array of specified no of elements
money=[10,20,30,40]
a,b,c,d=plt.bar(x,money).scatter(True)
a.set_facecolor('r')
b.set_facecolor('g')
c.set_facecolor('b')
d.set_facecolor('black')
plt.xticks(x,("A","B","C","D"))
plt.show()


import pandas as pd
df=pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])

df.plot.bar()
df.plot.bar(stacked=True)


#Plotting the datalines
from pandas.tools.plotting import parallel_coordinates
url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

names=['sepal-length','sepal-width','petal-length','petal-width','class']
dataset=pd.read_csv(url,names=names)
#Print dataset
plt.figure()
parallel_coordinates(dataset,'class')
print(dataset.groupby('class').size)

#Box plot
df1=pd.DataFrame(np.random.rand(10,5),columns=['A','B','C','D','E'])
color=dict(boxes='DarkGreen',whiskers='DarkOrange',medians='DarkBlue',caps='Gray')
df1.plot.box(color=color,sym='r+')


df1.plot.area()


