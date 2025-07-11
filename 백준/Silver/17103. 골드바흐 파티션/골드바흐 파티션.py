## 성능 개선 코드 
'''
1. 최대값을 활용하여 함수 호출 1번만 
2. bool을 이용하여 인덱싱 방식으로 리스트 방식에 비해 찾는 시간 줄임 (O(n) vs O(1))
'''

import sys
import math
input = sys.stdin.readline

# 소수 구하는 함수 정의 >> 소수 여부를 Bool로 구하여 성능 개선
def get_primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님
    
    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n))+1):
        # i가 소수라면 i의 배수는 소수가 아님
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # 소수 여부 Bool 배열 추출
    return is_prime

# 입력
T = int(input())
inputs = [int(input()) for _ in range(T)]  # 정수 n 리스트 생성
max_n = max(inputs)  # n 중 최대값 지정

# 최대값을 기준으로 소수 테이블 계산 
is_primes = get_primes(max_n)

# 골드바흐 파티션의 수 카운트 
for n in inputs:
    cnt = 0
    for num in range(2, (n//2)+1):
        if is_primes[num] and is_primes[(n-num)]:
            cnt+= 1
    print(cnt)
    
''' 이전 코드
import sys
import math
input = sys.stdin.readline

# 소수 구하는 함수 정의
def get_primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님
    
    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n))+1):
        # i가 소수라면 i의 배수는 소수가 아님
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # 소수만 추출
    return [i for i, val in enumerate(is_prime) if val]

# 입력
T = int(input())

# 골드바흐 파티션의 수 카운트 
for _ in range(T):
    n, cnt = int(input()), 0   # 정수 n 입력 및 변수 정의
    is_primes = get_primes(n)  # n보다 작은 소수 리스트 
    for num in range(2, (n//2)+1):
        if (num in is_primes) and ((n-num) in is_primes):
            cnt+= 1
    print(cnt)
'''