def solution(s):
    v=""
    j=0
    for i in range(len(s)):
        if s[i]==" ":
            j=0
            v=v+" "
        else:
            if j%2!=1:
                j+=1
                v=v+s[i].upper()
            else:
                j+=1
                v=v+s[i].lower()
        
    return v