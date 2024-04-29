
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    c=[]
    for i in range(len(A)):
        c.append(A[i]*B[i])
    answer = sum(c)


    return answer