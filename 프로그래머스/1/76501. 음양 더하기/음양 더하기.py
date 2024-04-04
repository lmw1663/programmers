def solution(absolutes, signs):
    sum=0
    for i in range(len(absolutes)):
        if(signs[i]==True):
            sum+=int(absolutes[i])
        else:
            sum-=int(absolutes[i])
    return sum