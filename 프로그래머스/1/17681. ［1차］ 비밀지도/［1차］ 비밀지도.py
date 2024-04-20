def solution(n, arr1, arr2):
    answer_bin = []
    for i in range(n):
        answer_bin.append((int(bin(arr1[i]),2) | int(bin(arr2[i]),2)))  
    print(answer_bin)
    new_list=[]
    for i in answer_bin:
        new_list.append(bin(i)[2:])
    answer=[]
    for i in range(len(new_list)):
        if len(new_list[i])!=n:
            str1 = '0'*(n-len(new_list[i]))
            new_list[i]=str1+new_list[i]
    
    print(new_list)

    for i in range(len(new_list)):
        str=''
        for j in range(len(new_list[i])):
            if(new_list[i][j]=='1'):
                str+='#'
            else:
                str+=' '
        answer.append(str)
    print(answer)
    return answer


