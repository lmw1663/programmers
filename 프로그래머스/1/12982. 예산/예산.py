def solution(d, budget):
    j=0
    sum=0
    d.sort()
    print(d)
    for i in d:
        sum+=i
        j+=1
        print(sum,j)
        if sum>budget:
            j-=1
            break

    print(j)
    return j