#Q1
i = 3
while(i<=7):
    print(i)
    i += 1



#Q2
n=int(input('enter your num'))
s=str(input('enter your str'))
i=0
while (i<=n):
    print(s*i)
    i+=n


#Q3
n=int(input("enter a num"))
i=0
z='*'
while(i<=n):
    print(z*n)
    n-=1


#Q4
i=0
sum1=0
sum2=0
n=int(input("plz enter your num"))
while(i<=n-1):
    n1=int(input("enter your num"))
    i+=1
    
    if n1%2==0:
        sum1+=n1
        ave_even=sum1/(i/2)
        
    else:
        
        sum2+=n1
        ave_odd=sum2/((i+1)/2)
        
print(ave_odd,ave_even)
        
        

