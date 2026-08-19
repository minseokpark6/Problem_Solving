import math 
def solution(n):
    if n < 2:
        return 0
    
    # 에라토스테네스의 체 변수 정의
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    
    # 소수 찾기 
    for i in range(2, math.isqrt(n)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    # 출력
    return sum(not x for x in is_prime[2:])
    
    
    
'''
def solution(n):
    answer = []
    temp = []
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                temp.append(i)
            
        if len(temp) >= 3:
            answer.append(i)
        temp = []
    
    return len(answer)
'''