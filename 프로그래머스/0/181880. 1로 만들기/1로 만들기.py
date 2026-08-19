def solution(num_list):
    # 변수 정의 
    cnt = 0
    
    # 연산 횟수 구하기
    for n in num_list:
        while n > 1:
            
            if n % 2 == 0:
                n = n // 2
            else:
                n = (n-1)//2
                
            cnt += 1
    # 출력
    return cnt