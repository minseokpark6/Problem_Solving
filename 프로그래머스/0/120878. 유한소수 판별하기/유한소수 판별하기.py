import math
def solution(a, b):
    # 기약 분수화
    if a == b:
        return 1
    c = b // math.gcd(a, b)
    
    # 분모의 소인수 확인 
    while True:
        if c %2 != 0:
            break
        c //= 2
    while True:
        if c%5 !=0:
            break
        c //= 5
    
    # 출력
    return 1 if c==1 else 2

"""
1. 기약 분수로 변경 후 분모의 소인수 중에 2와 5 외의 다른 수가 있는지만 확인하면 됨 
2. 기약 분수는 최대 공약수로 나누면 되고

"""


"""
# 시간 초과 

def get_factors(num):
    # 소인수 분해 
    factors = []
    d = 2
    while num > 1:
        if num % 2 == 0:
            factors.append(d)
            num //= 2
        else:
            d += 1
    # 출력
    return factors


def solution(a, b):
    # 변수 지정
    answer = 1
    big = max(a, b)
    
    # 기약 분수화 
    for i in range(2, big+1):
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i      
    
    # 분모 소인수 분해
    factors = get_factors(b)
    
    # 분모의 인수 확인
    if not all(x in [2,5] for x in factors):
        answer = 2
    
    # 출력
    return answer
"""