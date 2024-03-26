def solution(price, money, count):
    total_cost = price * count * (count + 1) // 2  # 등차수열의 합 공식을 이용하여 총 요금 계산
    return max(0, total_cost - money)  # 모자라는 금액 계산, 만약 부족하지 않으면 0 반환
