def solution(numbers, n):
    # 변수 정의
    result = 0
    
    # 출력
    for i in numbers:
        result += i
        if result > n:
            return result

'''
def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i 
        if answer > n:
            break
    return answer
'''