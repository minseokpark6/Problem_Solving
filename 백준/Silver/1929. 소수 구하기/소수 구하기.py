import sys 
import math 
input = sys.stdin.readline 
# 입력 
m, n = map(int, input().split())
# 소수 판별 함수 
def is_prime(x):
    if x<2:
        return False 
    for i in range(2, math.isqrt(x)+1):
        if x%i==0:
            return False 
    return True 
# 사이 수에 대한 소수 판별
for i in range(m, n+1):
    if is_prime(i):
        print(i)