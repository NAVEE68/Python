import nltk
nltk.download()

#To import the dataset
import pandas as pd
import numpy as np

data=pd.read_csv("C:/Users/Naveen/Desktop/Rbasics/Titanic/train.csv")
data

data.head()
data.head(10)

data.tail()

#To get the summary statistics
data.describe()

data.shape

v=data['Age']
v
v.head()
v.shape
v.dtype
v.mode()

data.size
#To transpose
data.T
data.head()

data.T
data.head()

#To get the indexes
data.axes

data['Age'].dtype
data.dtypes

data.empty
data.values

data.keys
data.sum()
data['Age'].mean()
data.mean()

data.std()
data.mode()
data['Embarked'].mode()
data['Survived'].mode()
data['PassengerId'].mode()
data['Sex'].mode()


data=data.rename(columns={'PassengerId':'PID','Survived':'Survival'})
data.head(10)


data.rename(columns={'Embarked':'embarked'},inplace=True)


df=pd.DataFrame(np.random.rand(5,3),index=[4,6,9,8,3],columns=['B','D','A'])
df

df.sort_index()
df.sort_index(axis=1)
df.sort_index(axis=1,ascending=False)

df.sort_values(by ='D')

df.sort_values(by =['D','A'])

df.sort_values(by ='D',kind='quicksort')

df.loc[:,'A']
df.loc[4,:]
df.loc[:,['A','D']]
df.loc[[4,9,3],['A','D']]
df.loc[:,'A']>0.25

df
#Indexes location
df.iloc[0,2]
df.iloc[:,2]

df.iloc[0,0:2]
df.iloc[0:2,0:2]

#df.ix  ( for both indexes and columns)

#To find the missing values in titanic dataset
data['Age'].isnull()

data['Age'].notnull()

#To find the sum of the missing values
sum(data['Age'].isnull())


#to replace the missing values
dataset=data.fillna(0)
dataset.head(10)


dataset1=dataset.dropna()
dataset1.shape


practice=pd.read_csv("C:/Users/Naveen/Desktop/Rbasics/Titanic/train.csv")
practice=practice.dropna()
practice.shape


practice=practice.dropna(axis=1)
practice.shape

df
df.append()

#To add a new column to the dataframe
df['Total']=df['A']+df['D']

df['E']=np.random.rand(5)


l=dataset['Age'][90:201]
l

l1=dataset[dataset['Age']>60][['Pclass','Age','Sex']]
l1


l2=practice[practice['Age'].isnull()][['Pclass','Age','Sex']]
l2


dataset.duplicated()
dataset.drop_duplicates()

dataset.info()
data.Age[0:5]
data['Age'][0:5]

data[['Survival','Age']][0:5]

data.describe()

data.Age

data['Survival'].value_counts()
#Percentages
data['Survival'].value_counts(normalize=True)*100

pd.crosstab(data.Sex,data.Survival)

pd.crosstab(data.Sex,data.Survival,normalize='Index')

tot=data[data.Age<=5]

len(tot)

data[data.Age<=5]['Survival'].value_counts()


data[data.Name.str.contains('Allen')]

data.embarked.unique()

data.embarked.value_counts(dropna=False)

data[(data.Survival==1)&(data.Age<=5)][['Pclass','Age','Survival']][0:5]

data.groupby('Pclass')['Age'].mean()
data.groupby('Pclass')['Age'].value_counts()


data.groupby('Survival')['Age'].mean()
data.groupby('Survived')['Age'].value_counts()



data.groupby(['Pclass','Sex'])['Age'].mean()

data.groupby(['Pclass','Sex'])['Survival'].sum()


data.groupby(['Pclass','Sex'])['Age'].mean().reset_index()


