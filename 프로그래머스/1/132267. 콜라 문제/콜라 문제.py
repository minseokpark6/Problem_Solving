def solution(a, b, n):
    # 변수 정의 
    cnt = 0 
    
    # 받을 수 있는 콜라 개수 카운트 
    while n//a > 0:
        exchange = n//a
        cnt += exchange*b
        n = exchange*b + (n%a)

    # 출력
    return cnt