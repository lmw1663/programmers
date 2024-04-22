def solution(n, m):
    nl=[]
    ml=[]
    for i in range(1,int((n/2))+1):
        if n%i==0:
            nl.append(i)
    for j in range(1,int((m/2))+1):
        if m%j ==0:
            ml.append(j)
    nl.append(n)
    ml.append(m)
    total=[]
    for i in nl:
        for j in ml:
            if(i==j):
                total.append(i)

    min1 = max(total)
    nl=[]
    ml=[]
    total=[]
    for i in range(1,n+1):
        ml.append(m*i)
    for j in range(1,m+1):
        nl.append(n*j)
    print(ml)
    print(nl)
    for i in ml:
        for j in nl:
            if(i==j):
                total.append(i)
    max1 = total[0]
    answer=[min1,max1]            
    return answer

