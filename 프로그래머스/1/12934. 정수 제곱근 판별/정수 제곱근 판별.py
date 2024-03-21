import math
def solution(n):
    t = math.sqrt(n)
    
    if t-math.floor(t)==0:
        return (t+1)*(t+1)
    else:
        return -1