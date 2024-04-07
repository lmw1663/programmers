def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j:
                answer.append(numbers[i]+numbers[j])
    set1 = set(answer)
    answer = list(set1)
    answer.sort()
    
    return answer