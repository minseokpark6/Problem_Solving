def solution(n):
    # 변수 지정 
    prev, curr = 0, 1
    
    # 피보나치 수 정의 
    for _ in range(2, n+1):
        prev, curr = curr, prev+curr 
    
    # 출력 
    return curr%1234567