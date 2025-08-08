import math 

# K진수로 변경하는 함수 정의 
def convert_to_n(num, base):
    result = ''
    
    while num>0:
        num, mod = divmod(num, base)
        result = str(mod) + result
    
    return result

# 소수 판별 함수 정의
def is_prime(n):
    # 0과 1 제외 
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False 
    return True

def solution(n, k):
    # K진수로 변환
    number = convert_to_n(n, k)

    # 0으로 분할 
    parts = number.split('0')
    
    # 소수 개수 카운트
    cnt = 0
    for part in parts:
        if part and is_prime(int(part)):
            cnt += 1

    return cnt