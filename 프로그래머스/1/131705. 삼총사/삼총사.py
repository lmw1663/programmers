def solution(number):
    answer = []
    for i in range(len(number)):
        for j in range(len(number)):
            for k in range(len(number)):
                if i!=j and j!=k and k!=i:
                    if number[i]+number[j]+number[k]==0:
                        str1=[]
                        str1.append(i)
                        str1.append(j)
                        str1.append(k)
                        str1.sort()
                        result_to_int = int(''.join(map(str, str1)))
                        answer.append(result_to_int)
    print(answer)
    answer1 = set(answer)
    
    return len(answer1)