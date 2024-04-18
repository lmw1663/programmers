def solution(s):
    v = []
    for i in s:
        v.append(ord(i))
    print(v)
    v.sort()
    s1=[]
    s2=[]
    for i in v:
        if(i<=90):
            s2.append(chr(i))
        else:
            s1.append(chr(i))

    s3="".join(list(reversed(s1))+list(reversed(s2)))
    
    return s3