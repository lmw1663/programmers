def solution(s):
    dic={"":""}
    a  =[]
    j=0
    for i in s: 
        if i not in dic:
            a.append(-1)
            dic[i] = j
        else:
            a.append(j-dic[i])
            dic[i] = j
            
        j=j+1
    print(a)
    print(dic)
    
    return a