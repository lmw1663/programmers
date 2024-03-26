def solution(left, right):
    result = 0
    for num in range(left, right + 1):
        # 약수의 개수가 짝수인지 확인
        if int(num**0.5) == num**0.5:
            result -= num
        else:
            result += num
    return result