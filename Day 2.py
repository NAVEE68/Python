import numpy as np
np.absolute(-56.6)

import math
print(math.sqrt(169))


#Day - 2
import numpy as np
a=np.array([1,2,3,4,5],float,)
print(a)
print(type(a))

#Int
b=np.array([1,2,3,4,5])
print(b)

#Sclicing on the array
a[:2]
a[:3]
a[1]
a[0:5]
a[-1]
a[-4:-2]


#2-d array
c=np.array([[1,2,3,4,5],[6,7,8,9,10]])
c
#Slicing
c[0,0]
c[0,3]
c[:,4]
c[0,1:4]
c[-1,-1]
c[-1,3]


c.shape#Like dim in R
a.shape

#To find the datatype of the array
a.dtype

len(a)
len(c)


d=c.copy()
d


e=np.array(range(10),float)
e.reshape((2,5))


8 in c
9 in d

print(e>3)
e


e[e>3]

b.tolist()
type(b)
f=list(b)
f[2]

g=b.tostring()
g

a[::2]
a[::3]


h=np.array(range(2,10),int)
h

a1=np.array([1,2,3])
a2=np.array([4,5,6])
a1+a2
a1-a2
a1*a2
a1/a2

a3=np.array([1,2,3,4])
a1*a3
len(a1)
sum(a1)
sum(a2)


a1**a2

#floor and ceil
x1=np.array([21.125,66.6])
x2=np.floor(x1)
x2
x2=np.ceil(x1)
x2

np.prod(a)
np.mean(a)
np.max(a)

np.median(a)

#To print the elements in 1d array
for val in a1:
    print(val)
    
#To print the elements in 2d array
    
for val in c:
    print(val)    
    
sum(c[0,:])

for i in c:
    print(sum(c[i:,]))    
    
z=c[ :,1:4]    

for i in z:
    print(i)
    

np.std(a2)
np.var(a2)


c.argmax()
c.mean(axis=0)
c.mean(axis=1)

c.sum(axis=0)
c.sum(axis=1)

z=np.array([[1,2,3],[4,5,6],[7,8,9]])
z.mean(axis=0)
z.mean(axis=1)
z.mean(axis=2)

z.unique()
z.shape

np.dot(a1,a2)
np.cov(a)
np.corrcoef(a)
np.std(a)
np.std(c)


a3=np.random.random()
a3

np.random.seed(638463)

np.random.rand(3)

np.random.rand(2,5)

import pandas as pd

v=pd.read_csv("C:/Users/Naveen/Downloads/IRIS.csv")
v

a3=np.array([1,2,3,4])
a4=np.array([0,0,2,3,3])
a3.take(a4)

a3.put([0,3,2],a4)

#To create a series 
data=np.array([1,2,3,4,5])
I=['a','b','c','d','e']
pd.Series(data,I)
pd.Series(data)

d2={1:10,2:20}
pd.Series(d2)

data1=10
pd.Series(data1,I)

data2=np.array([10,90,200,500,505,260])
I2=(['a','b','c','d','e','f'])
s=pd.Series(data2,I2)
s[3]
s['d']
s['c':'e']
s[2:5]

s[::2]
s['a','e','f']

s[-3]
max(s)


df={'one':pd.Series(data,I),
    'Two':pd.Series(data2,I2)}
df

data3=pd.DataFrame(df)
data3

I3=[1,2,3,4,5,6]

datalist=[{'a':1,'b':2},
          {'a':4,'b':5,'c':6},
          {'a':8,'b':9,'c':10}]
I=['First','Second','Third']
c=['a','b','c']

dataset=pd.DataFrame(datalist,I,c)
dataset



datalist2=[{'a':1,'b':2},
          {'a':4,'b':5,'c':6},
          {'a':8,'b':9,'c':10}]
I=['First','Second','Third']
c=['a','b','c1']

dataset=pd.DataFrame(datalist2,I,c)
dataset

dataset.to_csv('data.csv')

dataset['b']
dataset[0:3]