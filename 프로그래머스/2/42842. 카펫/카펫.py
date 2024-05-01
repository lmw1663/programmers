def solution(brown,yellow):
    yellow_divider = []
    for i in range(1,yellow+1):
        if yellow%i == 0:
            yellow_divider.append(i)
    if len(yellow_divider)%2 ==0:
        len1 = len(yellow_divider)/2
    else:
        len1 = len(yellow_divider)/2+1
    arr  = yellow_divider[0:int(len1)]

    sum_array = []
    for i in arr:
        sum = (yellow/i+2)*2 + i*2
        if sum==brown:
            sum_array.append(i)
            sum_array.append(int(yellow/i))

    return [sum_array[1]+2,sum_array[0]+2]
        