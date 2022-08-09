#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=1
while x<=5:
    print(x,end=',')
    x+=1
    


# In[2]:


x=1
sum=0
while x<=5:
    sum+=x
    x+=1
print(sum)


# In[8]:


x=5
sum=0
while x>=0:
    sum+=x
    x-=1
print(sum)


# In[11]:


while True:
    x,y=map(float,input().split ())
    if y==0:
        print("y is zero")
        break
    print(x/y)
print('bye')


# In[ ]:


while True:
    x,y=map(float,input().split ())
    if y==0:
        print("y is zero")
        continue
    print(x/y)
print('bye')


# In[1]:


n=int(input())
row=1
while row<=n:
    stars_count = 1
    
    while stars_count <= row :
        print('*',end='')
        stars_count+=1
    print()
    row+=1


# In[2]:


for pos in range(5):
    print(pos,end=' ')
print()


for pos in range(2,5):
    print(pos,end=' ')
print()


rng = range(1,21,4)
for pos in rng:
    print(pos,end=' ')
print()


# In[3]:


mystr='me!'
for char in mystr:
    print (char)


# In[4]:


for i in range (5):
    print(i)
else:
    print("no items left")


# In[5]:


print()
print(1,5,'hi')
ans=min(3,6)
type(15)
len('mostafa')
int('200')
s1=input()
s2=input('enter:')


# In[7]:


def our_print(first ,second):
    print('sum=',first+second)
    print('multi',first*second)
our_print(1,2)
print('oh')
our_print(3,4)


# In[10]:


#error
'''
def our_print(first,second):
print('sum=',first+second)
print('sub=',first-second)
'''
def our_print(first,second):
    print('sum=',first+second)
    print('sub=',first-second)
    


# In[14]:


def our_min(first, second):
    if first < second:
        return first
    else:
        return second 

def our_max(first, second):
    if first > second:
        return first
    return second

a , b = 5 , 20
print(our_min(a,b))
print(our_max(a,b))


# In[17]:


name = 'youssef'
def out():
    name = "ahmed"
    def inn():
        print(name)
    inn()
out()
print(name)


# In[21]:


def sum_two_number(y):
    x=2
    sum_of_numbers=x+y
    print(x)
    return sum_of_numbers

x=3
print(x)
sum_two_number(5)


# In[25]:


if int(input())<1000:
    lucky_number = 13
print(lucky_number)


# In[27]:


name="ahmed"
def outerfn():
    name = "ali"
    def innerfn():
        nonlocal name
        print(name)
        name="sara"
    innerfn()
    print(name)
outerfn()


# In[31]:


def our_sum(a,b):
    return(a+b)
our_sum('hel','lo')


# In[29]:


our_sum(6,10)


# In[32]:


def f(a, b, c):
    return a, b*b, c*c*c
 
ret = f(1, 2, 3)
x, y, z = ret
 
print(x + y + z)


# In[33]:


def f(a, b, c):
    return a, b*b, c*c*c
 
x, y, z, w  = f(1, 2, 3)
 
print(x + y + z)


# In[34]:


def f(n = 5, m):
    ret = 1
    while m > -2:
        ret *= n
    return ret
 
print(f(2))


# In[37]:


def a():
    return 10
def b(x = 5):
    return 2 * x + a() 
def c():
    print(b(3))
 
 
c()


# In[39]:


def f2():
    return 3 + f1(False)
 
def f1(go_deeper = True):
    if go_deeper:
        return 2 * f2()
    return 1
print(f2())


# In[42]:


my_str = '0123456789012345'
status = True
for idx, char in enumerate(my_str): 
    idx = str(idx % 10)
    if status and idx != char:
        status = False 
print(status)


# In[45]:


def f():
    global x
    x += 1
    return x
x = 10
print(f(), f(), f())


# In[49]:


x = 10
def f():
    x =5
    return x
f()
print(x)


# In[50]:


def f(k1, k2, k3 = 3):
    return k1 * k2 * k3 
print(f(k2='Hi', k1=2, 2))


# In[52]:


def f(a, b, c, /, d, e, *, f, g):
    return a + b+c+d+e+f+g


# In[53]:


def f():
    print('hello world')


# In[54]:


def f():
    print('hello world')
    f()


# In[55]:


def print_menu():
    while True:
        print('\n\nMenu:')
        print('Enter 1 to add 2 numbers')
        print('Enter 2 to subtract 2 numbers')
        print('Enter 3 to end the program')
 
        user_inp = input('\nEnter choice from 1 to 3: ')
 
        if user_inp not in '123':
            print('Invalid Input...Try again')
            continue
        else:
            return user_inp


# In[ ]:




