
def solution(arr):
    result = [arr[0]]  # 결과를 저장할 리스트에 첫 번째 원소 추가
    
    # 현재 원소와 이전 원소를 비교하여 연속된 숫자가 아닌 경우에만 결과 리스트에 추가
    for num in arr[1:]:
        if num != result[-1]:
            result.append(num)
    
    return result