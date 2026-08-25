def solution(n):
    # 변수 정의 
    factorial = 1
    i = 1
    
    # 조건에 만족하는 경우 찾기
    while factorial <= n:
        i += 1
        factorial *= i
    
    # 출력 
    return i - 1

            
'''
def solution(n):
    answer = 0
    while True:
        answer += 1
        temp = 1
        for i in range(1, answer+1):
            temp *= i
        
        if temp < n :
            continue
        elif temp == n:
            return answer
            break
        else:
            return answer - 1
            break
        
    
'''
    