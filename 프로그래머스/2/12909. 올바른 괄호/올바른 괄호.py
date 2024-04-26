def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i]=="(":
            answer.append("(")
        else:
            if len(answer)==0:
                return False
            else:
                answer.pop()
    if len(answer)==0:
        return True
    else:
        return False