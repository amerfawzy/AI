#!/usr/bin/env python
# coding: utf-8

# In[1]:


#conversions
m='10'
x=int(m)
y=float(m)

print(m,type(m))
print(x,type(x))
print(y,type(y))

f=28.7
t=int(f)
g=str(f)

print(f,type(f))
print(t,type(t))
print(g,type(g))


# In[10]:


str=input('enter your name')
print('hello'+str)
print('hello'+input('enter your name:'))


# In[15]:


#if-elif chain(1) 
salary = int(input())
if salary < 1000:
    print('you are poor')
elif 1000 <=salary < 20000:
    print('good salary')
else:
    print('your are rich')


# In[53]:


#if-elif chain(2) 
num=int(input())
if num < 10:
    print("1 digit")
elif num < 100:
    print("2 digit")
elif num < 1000:
    print("3 digit")
elif num < 10000:
    print("4 digit")
else:
    print("5+ digit")


# In[17]:


#if-elif chain(3) 
num = int(input())
if 100 <= num <= 200:
    print("let's go deeper")    
    if num%2 ==0:
        print("even number")        
        if num==150:
            print('150 is lucky number')            
    else:
        print('bye Mr odd')
else:
    print("have a good day")


# In[19]:


#while statment(1)
x=1
while x<= 5:
    print(x,end=',')
    x=x+1


# In[20]:


#while statment(2)
x=1
sum=0
while x<=5:
    sum+=5
    x+=1
print(sum)


# In[21]:


#while statment(3)
x=5
sum=0
while x>=0:
    sum+=x
    x-=1
print(sum)            


# In[50]:


while True:
    x,y = map(float,input().split())
    if y==0:
        print("y is zero!")
        break
    print(x/y)
print("bye")    


# 

# In[52]:


while True:
    x,y = map(float,input().split())
    if y==0:
        print("y is zero!")
        continue
    print(x/y)
    
print("bye")    


# In[46]:


t=int(input())
while t>0:
    n=int(input())
    sum=0
    start=1
    while start <= num:
        sum+=start
        start+=1
    t-=1
    print("sum from 1 to",num,"=",sum)


# In[41]:


n=int(input())
row = 1
while row <= n:
    stars_count = 1
    
    while stars_count <= row:
        print('*',end='')
        stars_count+=1
    print()
    row+=1


# In[62]:


#form while to for loops
for pos in range (5):
    print(pos,end=' ')
    
for pos in range (2,5):
    print(pos,end='')
print()    

rng = range(1,21,4)
for pos in rng:
    print(pos,end=' ')
print()

pos=0
while pos<5:
    print(pos,end=' ')

pos=0
while pos < 5:
    print(pos,end=' ')
print()


# In[63]:


#Iterating backward
for pos in range(5,0,-1):
    print(pos,end=' ')
print()

for pos in range(10 , 0 ,-2):
    print(pos,end=' ')
print()

for pos in range(5):
    pass

for pos in  range(5):
    ...


# In[68]:


mystr = 'amer'
for char in mystr:
    print(char)
"""
a
m
e
r
!
"""


# In[71]:


test_cases = int(input())
for case in range(test_cases):
    n,sum = int(input()),0
    for pos in range (1,n+1):
        sum+=pos
    print('sum from 1 to',n,'=',sum)    


# In[72]:


for i in range (5):
    print(i)
else:
    print('no items lest')
"""
0
1
2
3
4
no items left.
"""


# In[73]:


for i in range (5):
    print(i)
    if i == 3:
        break
else:
    print("if you break in the loop."
          "else is ignored")
"""
0
2
3
4
"""


# In[ ]:




