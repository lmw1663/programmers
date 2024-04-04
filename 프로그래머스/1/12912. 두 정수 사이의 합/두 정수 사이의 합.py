def solution(a, b):
    sum=0
    if(a>b):
        c=a
        a=b
        b=c
        
    for i in range(a,b+1):
        sum+=i
    return sum