def solution(array, commands):
    li1=[]
    for i in range(len(commands)):
        arr= array[commands[i][0]-1:(commands[i][1])]
        arr.sort()
        print(arr)
        li1.append(arr[commands[i][2]-1])
    print(li1)
    return li1