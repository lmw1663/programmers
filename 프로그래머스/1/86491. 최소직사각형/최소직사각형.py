def solution(sizes):
    l1 = []
    l2 = []
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            l1.append(sizes[i][1])
            l2.append(sizes[i][0])
        else:
            l1.append(sizes[i][0])
            l2.append(sizes[i][1])
    return max(l1)*max(l2)