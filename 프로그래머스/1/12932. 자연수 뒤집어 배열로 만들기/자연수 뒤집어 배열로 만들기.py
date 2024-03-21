def solution(n):
    answer=[]
    j = str(n)
    
    for i in j:
        answer.append(int(i))
    answer.reverse()
    return answer