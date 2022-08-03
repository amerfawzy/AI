total_cases=int(input())
for cases in range (total_cases):
    n,summ=int(input()),0
    
    for pos in range(n):
        value,result=int(input()),1
        for it in range (pos+1):
            result*=value
            summ+=result
        print(summ)

    
    
    