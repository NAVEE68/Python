"""
Guido Vasn Rossum
Beginning Python
Data Types
Sequences Types
"""

#int
x=5
print(x)
print(type(x))
x

#float
y=2.5
print(type(y))
y

#Char
s='Hello'
print(type(s))
s

#boolean
b=True
print(type(b))
b


#Sequence types
#lists
l=[1,3,5,'abc']
print(type(l))
l.append(2)
l[3]
l[0:5]
l[0:6]
l[2:]
l


l1=[1,'a',2,'b',3,'g',3,4,5,76,8,9,'we',(100,101)]
l1[3:]
l1[:5]
2 in l1

#tuple
t=('Ashwini',25,'BLR',True)

t1=t
t2=(3,6,7)
t1=t+t2
t=t+t2
t.append(2) #Gives an error
print(type(t))



#in operator
3 in t

8 not in t

"a" in s
'h' in s
'll' in s
'lol' in s
'l' not in s

#Arithmmetic operations
x+y
x*y
x-y
y-x
x/y
20%3
2^3 #Exponet
2**3#Power


#Adding 2 lists
list1=[2,3]
list2=[4,5]
print(list1+list2)

#Adding 2 tuples
tuple1=('a','b',6)
tuple2=('c','d',8)
print(tuple1+tuple2)

#Adding 2 strings
str1="Hello "
str2="World"
print(str1+str2)
str1.count

#'*' operator
t3=t1*2
t3

l*3

s*3

a=input()
print(a)

a=input(' ')
print(a)

a=input()
print(a)
print(a.upper())
print(a.lower())


b='Hi Annthamma'
print(b.lower())
print(len(b))

#To get the no of occurances of a specified char
print(b.count('a'))

#Gives the index of the first occurance of the specified char
print(b.find('a'))


print(b.isdigit())
print(b.isprintable())

b1=b.split()
b2="".join(b1)
print(type(b2))
print(type(b1))


str3='Python is fun'
str4=str3.split()
str5="".join(str4)
str4[-3]

#Task
str8=input()


if str8.isalpha():
    print(str8[2:].upper()+str8[:2].upper()+"J1")
    
else:
    print("Enter a valid string")
    
l3=[2,5,'g',5]
print(len(l3))
l3.append('hey')
print(len(l3))

l3.append(2)
l3.count(2)


l3.remove(5)
del l3[1]
l3[2]=3
l3.insert(6,19)
l3[3]

#For adding tuple to the list
l3.extend(t)
l3

#To convert tuple to a list
l4=list(t1)
print(l4.reverse())
l4

l4.sort()
l5=[8,2,9]
l5.sort()
l5.pop()

l5.pop(0)


l6=['e','a','z']
l6.sort()
l6.pop()

l7=[2,5,7,9]
max(l7)
min(l7)
sum(l7)


l8=['a','k','o']
max(l8)
sum(l8)

for val in l7:
    print(val)



for val in l8:
    print(val)

t[2]
t[2:]
t[:3]

t.index('BLR')

t7=(2,9)
t8=(3,5)
t9=t7+t8
t9



del t7

max(t3)
t10=tuple(l3)
print(type(t10))



#Dictionaries
d={'Name' : 'Navi', 'Occupation': 'Student','empid':233,'email':'xy@gmail.com'}
d['contact']=2314834934

del d['Occupation']


d.items()
d.keys()
d.values()

d1=d

d.clear()


d['Name']
d.get('empid')

d['ahdhh']
d.get('sdkjdks')
d['age']=52

d['age']=50

for val in d.values():
    print(val)
    


list6=['aus','us','ind','sl','china','sin']
list7=['10M','35M','85M','22M','98M','65M']
d4=zip(list6,list7)
d5=dict(d4)    
d5