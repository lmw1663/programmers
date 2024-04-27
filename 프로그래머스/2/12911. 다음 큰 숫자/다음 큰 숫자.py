def solution(n):
    num_s = (bin(n)[2:])
    onum =  num_s.count('1')
    i=1
    while True:
        new_num_s = (bin(n+i)[2:])
        new_num = new_num_s.count('1')
        if new_num == onum:
            break
        i+=1
    
    return n+i