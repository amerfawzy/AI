#!/usr/bin/env python
# coding: utf-8

# In[21]:


#Q1
class Natural_number_class(object):
    def sum_100_natural_numbers(self):
        for i in range(5, 10,1):
            print(i)
        print("-")
        for j in range(5, 10,2):
            print(j)         
    
#Create an Object 
object_sum = Natural_number_class()
print(object_sum.sum_100_natural_numbers())


# In[24]:


#Q2 Sum from 1 to N 1st way
class Natural_number_class(object):
    def sum_100_natural_numbers(self):
        n=int(input())
        sum = 0
        for i in range(1, n):
            sum = sum + i
        return sum
#Create an Object
object_sum = Natural_number_class()
print(object_sum.sum_100_natural_numbers())


# In[28]:


#Q2 Sum from 1 to N 2nd way
class natural_number_class(object):
    def sum_100_natural_numbers(self):
        n=int(input())
        total = sum(range(1, n))
        return total
object_sum = natural_number_class()
print(object_sum.sum_100_natural_numbers())


# In[48]:


#Q3 Datetime review
from datetime import datetime
class DataTime(object):
    def __init__(self,now):
        self.now = datetime.now()
        print(now)
object_DateTime = DataTime(now)


# In[37]:


from datetime import datetime
now = datetime.now()
print(now)


# In[5]:


class car(object):
    def __init__(self,engine,fourwheels):
        self.engine = engine
        self.fourwheels = fourwheels
x=car("motor","wheels")
print(x.engine,x.fourwheels)


# In[6]:


class sound:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
   
x=sound("cat","sd")
y=sound("monkey","sdd")
z=sound("whale","qwwe")
print(x.name,x.sound)      
print(y.name,y.sound)      
print(z.name,z.sound)      


# In[7]:


class shape():
    def __init__(self,cle,sqr,tri):
        self.cle=cle
        self.sqr=sqr
        self.tri=tri
    def __threeD__(self,sph,cube,tth):
        self.sph=sph
        self.cube=cube
        self.tth=tth
z=int(input("enter number of D.s "))
if z==2:
    x=shape("circle","square","triange")
    print(x.cle,x.sqr,x.tri)    
else:
    y=shape("sphere","cube","tetrahedron")
    print(y.cle,y.sqr,y.tri)


# In[1]:


class communitymember:
    def __init__(self,student):
        self.student=student
    def __DECC__(self,alumnuns):
        self.alumnuns=alumnuns
    def __emp__(self,employee):
        self.staff=staff
        self.faculty=faculty
    def __faculty__(adminstrator, teacher):
        self.adminstrator = adminstrator
        self.teacher = teacher
y=communitymember("osama")
print(y.student)


# In[21]:





# In[ ]:




