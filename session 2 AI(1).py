#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('love' < 'zebra')
print('love' < 'long')
print('love'!= 'long')


# In[4]:


print('counter' < 'counter')


# In[4]:


x=str(input("enter your name"))
y=len(x)
print(y)


# In[12]:


name=input("enter your name")
def name(name):
    name=str(input("enter your name"))
    y=len(name)
    return name


# In[5]:


name= input('enter your name')


# In[4]:


type(name)


# In[10]:


str=5
print(str)


# In[15]:


x='amer'
print('a'in x)
print('am'in x)
print('ame'in x)
print('amx'in x)
print('amet'not in x)


# In[17]:


salary=int(input())
if salary<1000 :
    print('you are poor')
else:
    print("you are rich")
    
print("work hard")


# In[19]:


x=int(input("enter your salary"))
if x<1000:
    print("poor")
elif 1000<x<20000:
    print('good salary')
elif 20000<x<50000:
    print('rich')
else:
    print("3la 7sb")
        


# In[1]:


#extra examples
#=========================
#8888888888888888888888888


# In[3]:


#printing
print('hello py')
print("hello py")
"""
lets start 
some basics again 
try to be patient for leaning more :)
"""


# In[4]:


print(1+2+3)
print(3*4)
print    (6/2)
print('6/2')


# In[5]:


#arithmatic operations
x=6
y=3
#binary operator
print(x+y)
print(x+2 * y-1)
print(x/y)
z=(x+y)/3/3
print(z)
#unary operator
print(-z)


# In[7]:


#binary and unary operations 
print(7)        #7
print(+7)       #7
print(+++7)     #7

print(-7)       #-7
print(--7)      #7
print(---7)     #-7
print(----7)    #7

print(7 -- 5)   #12
print(7 --- 5)  #2




# In[9]:


print(14/2)  #7.0
print(14/3)  #4.666666666666667
print(13/40) #0.35

print(14//2)  #7
print(14//3)  #4
print(14//40) #0

print(14/8)  #1.75
print(14//8) #1 round down to a small value 1=min(1,2)
print(-14//8) #-2= -2 = min(-2,-1)

print(type(14/7))   #float
print(type(14//7))  #int


# In[10]:


n = 12345

print(n / 100)        #1234.5
print(n / 1000)       #123.45
print(n / 10000)      #12.345
print(n / 100000)     #1.2345
print(n / 1000000)    #0.12345

#remove last digits
print(n // 100)      #1234
print(n // 1000)     #123
print(n // 10000)    #12 
print(n // 100000)   #1
print(n // 1000000)  #0



# In[12]:


print(2**4)    #16
print(2**-4)   #0.0625 = 1/16

print(5**0)    # 1
print(0**5)    #0

print(2.1**4)  # 19.448100000000004 
print(2**4.1)  #17.148375400580687

#remove last k digits
n,k=12345,3
print(n//(10**k))  #12


# In[13]:


# x is left hand side (has address)
#1 + 2 * 5 = right hand side = an expression 
x = 1 + 2 * 5   #11

x -= 4          #7: x=x-4  
x += 3          #10: x=x+3
x *= 2          #20: x=x*2  
x //=5          #4: x=x//2
x **=3          #64: x=x**3
x %=6           #6: x=x%6
 


# In[14]:


#multiple assignments
x,y = 5,7
a,b,c = 'hi' ,12, 6.5

x=y=z=1
#x =y =z +=1 #invalid

m=3
print(10*m,m+1)
m,n = 10*m ,m+1
print(m,n)


# In[15]:


#comma in printing("there is",1,"instructor not",2*3) 
print("there is",1,"instructor not",2*3)


# In[16]:


#boolean data type
status = True
print(status)
print(not status)

print(bool('0'))
print(bool('1'))
print(bool(''))

print(bool(5))
print(bool(-5))
print(bool(5.5))
print(bool(0))


# In[22]:


#True or False
print(bool(3 > 5))
print(bool(3 < 5))
print(bool(3 == 5)) 
print(bool(3 >= 5))
print(bool(3 >= 3))
print(bool(3 == 3))
print(bool(3 > 1))
print(bool(3 != 4))
print(bool(3 != 3))


# In[23]:


#comparing strings
#if a word has a smaller letter:it appears frist
print('love' < 'zebra')
print('love' < 'long')
print('love' != 'long')
#if one worf is done in comparison:the smaller in length comes first
print('counter' < 'counterattack')
#upper letters are smaller than small letters
print('A' < 'a')
print('A' < 'z')
print('Z' < 'a')
print('loVE' < 'a')
print('loVE' < 'long')


# In[24]:


#comparing strings 
print('' < 'A')

print(' ' < 'A')
print(' ' < 'a')

print('0' < 'A')
print('0' < 'a')


# In[25]:


#comparing floating point
a=3/7
b=0.1 + 3/7 - 0.1

print(a)
print(a)
print(a==b)

x=5.00000000000000
y=4.9999999999999999999999999999999999
print(x==y)


# In[27]:


#operator precedence
print (1+2 == 3)
print (16 == 2**4)


# In[28]:


#variable assignments
print(55)
age=55
print(age)
print(age+5)
weight = 75.8
print(weight)


# In[29]:


#string manipulation 
print('i am amer')
print('i am'+' '+'amer') 

str1 = 'i am'
str2 = 'amer'
print(str1+str2)

str3 = 'hello'
str4 = str1+str2+str3
print(str4)
print(str1*3)
print(2*str1+str2)

print('hello\tworld')
print('hello\t\tworld')


# In[30]:


#max and min functions 
a=min(3,4)
print(a)

s=min(3,6,-2)
print(s)

e=max(9,6,-2,15)
print(e)

print(max(4,7))
print(max(4,7)+2)


# In[36]:


#type function
print=(type('20.5'))


# In[35]:


print(type(15))


# In[37]:


print(type(20.5))

