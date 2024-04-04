def solution(x):
    # x를 문자열로 변환하여 각 자릿수를 리스트에 저장
    digits = [int(digit) for digit in str(x)]
    # 자릿수의 합 계산
    digit_sum = sum(digits)
    # x가 자릿수의 합으로 나누어지는지 검사
    if x % digit_sum == 0:
        return True
    else:
        return False