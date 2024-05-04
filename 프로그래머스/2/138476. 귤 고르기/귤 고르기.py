def solution(k, tangerine):
    
    li1 = []
    tangerine.sort()
    a = 1
    if len(tangerine)!=1:
        for i in range(len(tangerine)-1):
            if tangerine[i] != tangerine[i+1]:
                li1.append(a)
                a=0
            a+=1
            if i==len(tangerine)-2:
                li1.append(a)
    else:
        return 1
    li1.sort(reverse=True)    
    i=0
    sum=0
    while sum<k:
        sum+=li1[i]
        i+=1
    return i
print(solution(4,[1, 3, 2, 5, 4, 5, 2, 3]))