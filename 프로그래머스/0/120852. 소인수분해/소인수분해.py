def solution(n):
    # 변수 정의
    result = []
    i = 2
    
   # 소인수 구하기
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            
            # 중복 인수 제거
            while n % i == 0:
                n //= i

        i += 1
    if n > 1:
        result.append(n)
    # 출력
    return result
        
    

'''
def solution(n):
    answer =  []
    d = 2

    while n > 1:
        if n % d == 0:
            answer.append(d)
            n //= d
        else:
            d += 1
    
    return sorted(list(set(answer)))
'''