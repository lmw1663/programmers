def solution(n):
    count = 0
    
    # 시작점을 1부터 n까지 변경하며 연속된 자연수의 합이 n이 되는지 확인
    for start in range(1, n + 1):
        num_sum = 0
        num = start
        
        # 연속된 자연수의 합이 n이 되는지 확인
        while num_sum < n:
            num_sum += num
            num += 1
            
            # 합이 n이 되면 경우의 수(count)를 증가시키고 반복문 종료
            if num_sum == n:
                count += 1
                break

    return count