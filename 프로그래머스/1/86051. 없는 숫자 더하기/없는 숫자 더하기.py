def solution(numbers):
    # 없는 수 찾기 
    result = [i for i in range(10) if i not in numbers]
    # 출력
    return sum(result)