#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[2]:


import numpy as np 
a = np.array([2,3,4])
print(a)
print(type(a))


# In[5]:


b=np.array([1.2,3.5,5.1])
print(b)


# In[8]:


x = np.array([8,9,5])
print(f"x={x}")


# In[12]:


np.zeros(8)
#np.empty(8)


# In[13]:


np.ones(8)


# In[29]:


a = np.arange(5, 35, 5)


# In[30]:


b = np.arange(0 , 2 , 0.3)


# In[31]:


b


# In[32]:


a


# In[33]:


a.size


# In[34]:


b.size


# In[36]:


y = np.array([ 0 ,20 ,40 ,60 ,80 ,100])
y


# In[38]:


yy=np.arange(0,121,20)
yy


# In[39]:


np.linspace(0,2,9)


# In[46]:


from numpy import pi
f = np.sin(np.linspace(0, 2*pi, 10))
print(f) 


# In[50]:


a = np.array ([1 ,7 ,9 ,4])
b = np.array ([5 ,2 ,3 ,8])
c = np.concatenate((a,b))
c


# In[51]:


a.ndim #no of dimentions 


# In[52]:


a.size #total no of array equal to the product of elements of shape


# In[54]:


b.dtype # types of elements in array


# In[56]:


a = np.array([1,2,3,4,5,6,7])
a.shape


# In[57]:


row_vector = a[np.newaxis, :]
row_vector.shape


# In[58]:


col_vector = a[:, np.newaxis]
col_vector.shape


# In[59]:


b = np.expand_dims(a, axis=1) #axis=1 col vector
b.shape


# In[60]:


x = np.expand_dims(a, axis=0) #axis=0 row vector
x.shape


# In[66]:


#Basic vector operations
a = np.array( [20,30,40,50] )
b = np.arange(4)
print(b)
print(a)

c=a-b     #sub to vectors
print(c)
   
b**2      #squaring vector elements 
print(b**2)

d = 10*a  #multiplication with a scalar 
print(d)

print(a<35)   #logical operations  


# In[67]:


b = np.arange(3)
print(b)

print(np.exp(b))
print(np.sqrt(b))
print(np.sin(b))

c = np.array([2 ,-1 ,4])
print(np.add(b,c))


# In[69]:


a = np.arange(10)**3
print(a)
print(a[2])
print(a[2:5])


# In[70]:


#equivalent to a[0:6:2] = 1000;
#from start to position 6, exculsive, set every 2nd element to 1000
a[:6:2]=1000
print(a)


# In[71]:


a[::-1]
print(a)
for i in a:
    print(i**(1/3))


# In[78]:


x = np.array([1,2], dtype=np.float64)
y = np.array([7,8], dtype=np.float64)

# elementwise sum; both produce the array
print("the summation",x + y)
print(np.multiply(x,y))
print("the multiply",x * y)
print(np.multiply(x,y))
print("the subtraction",x - y)
print(np.multiply(x,y))
print("the division",x / y)
print(np.multiply(x,y))


# In[79]:


print(x.dot(y))
print(np.dot(x,y))
print(x @ y)


# In[81]:


print(x**2)
print(np.sqrt(x))


# In[82]:


np.exp(x)


# In[83]:


np.maximum(x,y)


# In[85]:


#plotting vectors
import matplotlib.pyplot as plt

v = np.array([[3,5],[0,5],[4,0],[3,3],[0,2]])
origin = np.array([[0,0,0,0,0],[0,0,0,0,0]])

plt.quiver(*origin,v[:,0] ,v[:,1] ,color=['r','b','g','y','m'],scale=15)
plt.show()


# In[92]:


#creating matrix

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

#elementwise sum;both produce the array
print("the summation",x + y)
print(np.add(x ,y))
print("the subtraction",x - y)
print(np.subtract(x ,y))
print("the multiplication",x * y)
print(np.multiply(x ,y))
print("the divison",x / y)
print(np.divide(x ,y))


# In[93]:


print(np.sqrt(x))


# In[104]:


rg = np.random.default_rng(1) #create a random variable of generator
a = np.floor(10*rg.random((3,4)))
print("the matrix\n",a)
print("the shape\n",a.shape)
print("the transpose \n",a.T) #transpose
print("the shape transpose\n",a.T.shape)


# In[3]:


#matrix multiplication 
a = np.array([[1,1],[0,1]])
b = np.array([[2,0],[3,4]])
np.matmul(a,b)


# In[5]:


a@b


# In[7]:


print(a.dot(b))
print(np.dot(a,b))


# In[8]:


rg = np.random.default_rng(1) #create instace of default random number generator 
m = rg.random((2,3))
print(m)
print(m.sum())
print(m.min())
print(m.max())


# In[13]:


print("the sum\n",m.sum())
print("the matrix\n",m)
print("the sum of each col\n",m.sum(axis=0))
print("the min of each row\n",m.min(axis=1))


# In[15]:


#printing multidimentional array
a = np.arange(6) #1d array
print(a)


# In[16]:


b = np.arange(12).reshape(4,3) #2d array
print(b)


# In[18]:


c = np.arange(24).reshape(2,3,4) #3d array
print(c) 


# In[28]:


#indexing ,slicing and iterating two dimentional array
def f(x,y):
    return 10*(x+y)
b = np.fromfunction(f,(5,4),dtype=int)
print(b)
print(b[2,3])
print(b[0:5,1])
print(b[:,1])
print(b[1:3, : ]) 


# In[29]:


b[-1]


# In[36]:


c = np.array(    [[[0,1,2],  # a 3D array(two stacked 2D arrays)
              [10, 12, 13]],
           [[100, 101, 102],
             [110,112,113]]])
print(c.shape)
print(c[1,...])  # same as c[1,:,:] or c[1]
print(c[...,2])  # same as c[:,:,2]


# In[38]:


for element in b.flat:
    print(element)


# In[39]:


#changing the shape of a multidimentional array
m1 = np.floor(10*rg.random((3,4)))
print(m1)
print(m1.shape)


# In[40]:


m1.ravel()


# In[42]:


m1.reshape(6,2)


# In[47]:


m1.reshape(4,-1)
print(m1.reshape(4,-1))
print(m1)


# In[49]:


m1.resize(2,6)
print(m1)

