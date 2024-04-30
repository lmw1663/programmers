def solution(n):
    va  =  [0,1]
    for i in range(n-1):
        va.append(va[i]+va[i+1])
    return va[n]%1234567

