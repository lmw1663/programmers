def solution(arr, divisor):
    li = []
    for i in arr:
        if i%divisor == 0:
            li.append(i)
    li.sort()
    if len(li)==0:
        li.append(-1)
    return li