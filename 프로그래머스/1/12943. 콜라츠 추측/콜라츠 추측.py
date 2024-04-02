def solution(num):
    n=0
    for i in range(500):
        if(num==1):
            return n
        if num%2==0:
            num=num//2
            n+=1
            print(num)
        else:
            num=num*3+1
            n=n+1
            print(num)
    return -1