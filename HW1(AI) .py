#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Q1
x=int(input("enter 1st num"))
y=int(input("enter 2nd num"))
print('the addition is:',x+y)
print('the subtraction is:',x-y)
print('the multiplication is:',x*y)
print('the dividion is:',x/y) 


# In[22]:


#Q1***
x=int(input("enter 1st num"))
y=int(input("enter 2nd num"))
if x%2==0:
    print("1st num is even")
elif x==0:
    print("1st num is 0")
elif x<0:
    print("1st num is -ve")
        
if y%2==0:
    print("2nd num is even")
elif y==0:
    print("2nd num is 0")
elif y<0:
    print("2nd num is -ve")

a=str(input("enter the operation"))
if a=='+':
    print("the sum is:",x+y)
elif a=='-':
    print("the subtraction is:",x-y)
elif a=='*':
    print("the multiplication is:",x*y)
elif a=='/':
    print("the dividion is:",x/y)
else:
    print("the operation is undifined")


# In[26]:


#Q2
s1=str(input("enter your name"))
g1=int(input("enter your garde"))
id1=int(input("enter your id"))
s2=str(input("enter your name"))
g2=int(input("enter your garde"))
id2=int(input("enter your id"))
print("information for students and thier 'math' gardes")
print(s1,"id",id1,"got grade",g1)
print(s2,"id",id2,"got grade",g2)
print("average math garde is",(g1+g2)/2)


# In[71]:


#Q3
NumList = []
Even_Sum = 0
Odd_Sum = 0
j = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

while(j < Number):
    if(NumList[j] % 2 == 0):
        Even_Sum = Even_Sum + NumList[j]
    else:
        Odd_Sum = Odd_Sum + NumList[j]
    j = j+ 1

print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
print("The Sum of Odd Numbers in this List =  ", Odd_Sum)


# In[72]:


#Q3***
EvenSum=0
OddSum=0
mylist=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(mylist)):
    if i%2==0:

        EvenSum+=mylist[i]

    else:

        OddSum+=mylist[i]
print(EvenSum)

print(OddSum)
          


# In[106]:


#Q4
x=int(input("enter number of repition"))
y1=str(input("enter your 1st sentence"))
y2=str(input("enter your 2nd sentence"))
y3=str(input("enter your 3rd sentence"))
u=x*(y1+"'"+y2+"''"+y3+"''")
print(u)


# In[111]:


#Q5
x,y=map(int,input().split())
print(y,x)

