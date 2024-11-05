def solution(n):
    # 변수 지정
    a, b = 0, 1
    
    # 피보나치 수(2 이상의 수 부터) 
    for _ in range(2, n+1):
        a, b = b, a+b

    # 출력
    return b % 1234567