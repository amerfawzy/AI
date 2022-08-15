#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Q1
#1)practice makes perfect.
2)'''
childeren must be taught 
how to think
not
what to think
'''
#3)2*3*4*5/10=
#4)12


# In[2]:


#Q2
x='print("me")'
print(x)
y="print('me')"
print(y)
a="print" + "('" + 'me")'
print(a)
print("you will learn \na lot")


# In[3]:


#Q3
n=int(input("enter number of rows"))
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print("\n")    


# In[4]:


#Q4
rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows-1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()


# In[5]:


#Q5
rows = int(input("Enter Diamond Pattern Rows = "))

print("Diamond Star Pattern") 
k = 0
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(end = ' ')
    while k != 2 * i - 1:
        print('*', end = '')
        k = k + 1
    k = 0
    print()

k = 2
l = 1
for i in range(1, rows):
    for j in range(1, k):
        print(end = ' ')
    k = k + 1
    while l <= (2 * (rows - i) - 1):
        print('*', end = '')
        l = l + 1
    l = 1
    print()
    


# In[8]:


#Q7
#CORRECTION

print("hi")
print()
print("i am mahmoud")
print(3*6)
print("wonderful day")
print("wonderful day")


# In[ ]:




