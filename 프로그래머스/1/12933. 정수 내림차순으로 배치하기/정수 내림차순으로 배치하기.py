def solution(n):
    a=[]
    for i in str(n):
        a.append(int(i))
    a=sorted(a)
    result =0
    j=1
    for i in a:
        result= result+(i*j)
        j=j*10
    print(result)
    return result