#!/usr/bin/env python
# coding: utf-8

# In[2]:


#HW1
y=int(input())

def print_menu():    
    
    print_menu(y)

if y==0:
    def sum_1_to_n():
        x=1
        sum=0
        while x<=4:
            sum+=x
            x+=1
        print(sum)
    sum_1_to_n()
    
if y==1:
    x=str(input())
    if x=='+':
        def addNumber(a, b):
            sum = a + b
            return sum
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        sum = addNumber(num1, num2)
        print("Sum of two numbers is: ", sum)
    elif x=='-':
        def subNumber(a, b):
            sum = a - b
            return sum
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        sub = subNumber(num1, num2)
        print("sub of two numbers is: ", sub) 
    else:
        def multNumber(a, b):
            sum = a * b
            return sum
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        mult = multNumber(num1, num2)
        print("multi of two numbers is: ", mult)         


# In[3]:


#HW2
a=int(input("enter number of your numbers"))
if a==2:    
    def maximum_2(a,b):        
        return max(a,b) 
    a=int(input("enter 1st num"))
    b=int(input("enter 2nd num"))
    print("max number is",maximum_2(a,b))
if a==3:
    def maximum_3(a, b, c):      
       list = [a, b, c] 
       return max(list) 
    x = int(input("Enter First number"))
    y = int(input("Enter Second number"))
    z = int(input("Enter Third number"))
    print("Maximum Number is",maximum_3(x, y, z)) 
if a==4:
    def maximum_4(a, b, c,d):      
       list = [a, b, c,d] 
       return max(list) 
    x = int(input("Enter First number"))
    y = int(input("Enter Second number"))
    z = int(input("Enter Third number"))
    d = int(input("Enter fourth number"))
    print("Maximum Number is",maximum_4(x, y, z,d)) 
if a==5:
    def maximum_5(a, b, c,d,e):      
       list = [a, b, c,d,e] 
       return max(list) 
    x = int(input("Enter First number"))
    y = int(input("Enter Second number"))
    z = int(input("Enter Third number"))
    d = int(input("Enter fourth number"))
    e = int(input("Enter fifth number"))
    print("Maximum Number is",maximum_5(x, y, z,d,e)) 
if a==6:
    def maximum_6(a, b, c,d,e,f):      
       list = [a, b, c,d,e,f] 
       return max(list) 
    x = int(input("Enter First number"))
    y = int(input("Enter Second number"))
    z = int(input("Enter Third number"))
    d = int(input("Enter fourth number"))
    e = int(input("Enter fifth number"))
    f = int(input("Enter sixth number"))
    print("Maximum Number is",maximum_6(x, y, z,d,e,f)) 


# In[4]:


#HW3
a=int(input("enter your number: "))
for i in range(2,a):
    if a%i !=0:
        continue
    else:
        print("Its not a prime number")
        break 
else:
    print("Its a prime number")
    print("the count is",i)    


# In[5]:


#Q4
def fib(n): 
    f = [0, 1]       
    for i in range(2, n): 
        f.append(f[i-1] + f[i-2]) 
    return f          
num = int(input("Enter number : ")) 
print(*fib(num))


# In[ ]:


#Q1
def repeatLetters(word):
    initialString = ""
    for i in range(len(word)):
        value = word[i] * (i + 1)
        initialString = initialString + value
    print(initialString)

repeatLetters("Amer fawzy")

