def solution(a, b, n):
    # 변수 지정
    answer = 0
    
    # 받을 수 있는 콜라병 개수 카운트
    while n//a > 0:
        answer += (n//a)*b
        n = (n//a)*b + (n%a)

    # 출력 
    return answer