print("menu")
print("enter 1 to sum numbers from 1 to n")
print("enter 2 to evaluate simple 2 numbers (e.g. 2+3)")
print("enter 3 to end the program")
n=int(input("enter your choice from 1 to 3"))
if n==1:
   n1=int(input("max numbers you want to sum"))
   i=0
   sum=0
   for i in range (n1):
       sum+=i
       print(sum)

elif n==2:
    s=str(input("enter your operation"))
    x=int(input("enter your 1st num"))
    y=int(input("enter your 2nd num"))
    if s=='+':
        print('the sum is',x+y)
    elif s=='-':
        print('the sub is',x-y)
    elif s=='*':
        print('the mult is',x*y)
    else:
        print('operation is unkown')

elif n==3:
    exit()
        
        
        
        

       
             
        