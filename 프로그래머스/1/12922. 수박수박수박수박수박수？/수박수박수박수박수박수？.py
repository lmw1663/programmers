def solution(n):
    str1=""
    for i in range(n):
        if i%2==0:
            str1+="수"
        else:
            str1+="박"
    return str1