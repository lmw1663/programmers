def solution(t, p):
    str1=""
    answer = 0
    for i in range(len(t)-len(p)+1):
        for j in range(len(p)):
            str1+=t[i+j]
        print(str1)
        if int(str1)<=int(p):
            answer+=1
        str1=""
        j=0
        
    return answer
