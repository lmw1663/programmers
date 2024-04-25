def solution(s):
    answer = s.split()
    answer1 = []
    for i in answer:
        answer1.append(int(i))
    answer1.sort()
    print(answer1)
    answer2=""
    answer2=str(answer1[0])+" "+str(answer1[len(answer1)-1])
    
    
    
    
    return answer2