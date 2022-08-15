#!/usr/bin/env python
# coding: utf-8

# In[1]:


class employee:
    name = None
    salary = None
    address = None
    
    def print(self):
        print('employee name',self.name)
        print('employee salary',self.salary)
        print('employee address',self.address)
    
    def read(self):
        self.name = input('enter name: ')
        self.salary = float(input('enter salary: '))
        self.address = input('enter address: ')
        
mostafa = employee()
mostafa.read()
mostafa.print()


# In[2]:


def print_empl(object):
    print('employee name: ',object.name)
    print('employee salary: ',object.salary)
    print('employee address: ',object.address)
def read_empl():
    obj=employee()
    obj.name=input('enter name: ')
    obj.salary=float(input('enetr salary: '))
    obj.address=input('enter address: ')
    
    return obj
mostafa = read_empl()
print_empl(mostafa) 


# In[8]:


class fullname:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.middle_name = None
        self.last_name = last_name

class employee:
    def __init__(self,first_name,salary,last_name,address):
        self.fullname = fullname(first_name,last_name)
        self.salary = salary
        self.address = address
        
    def print(self):
        print('employee name:',self.full_name.first_name + " " + self.full_name.last_name)
        print('employee salary:',self.salary)
        print('employee address:',self.address)
        
mostafa = employee('ziad','mostafa',159,'55 BC')
mostafa.print()


# In[9]:


class employee:
    def __init__(self,name,age):
        
        self.name = name
        self.age = age

most = employee('mostafa' , 33)
print(most)


# In[14]:


class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return ('employee' + self.name + ' is ' + str(self.age)+ ' years old ' )
most = employee('mostafa', 33)
print(most)
s=str(most)
print(most.__str__())


# In[18]:


class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name,self.age
most = employee('mostafa',33)
print(most.__str__())
print(str(most))


# In[20]:


class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return ('employee' + self.name + 'is' + str(self.age) + 'years old')
    
    def __repr__(self):
        
        return ('employee' + self.name + 'is' + str(self.age)+'years old'+'**')
most = employee('mostafa', 33)
print(str(most))
print(repr(most))


# In[21]:


class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return ('employee' + self.name + 'is' + str(self.age) + 'years old')
    
    def __repr__(self):
        
        return ('employee' + self.name + 'is' + str(self.age)+'years old')
most = employee('mostafa', 33)
print(str(most))
print(repr(most))


# In[ ]:




