import sys
import math 
input = sys.stdin.readline

# 입력 
n = int(input())

# 소수 판별 함수 
def is_prime(x):
    if x < 2:
        return False 
    for i in range(2, math.isqrt(x)+1):
        if x%i==0:
            return False 
    return True
    
# 입력 값보다 크고, 가장 작은 소수 찾기
for _ in range(n):
    num = int(input())
    while True:
        if is_prime(num):
            print(num)
            break
        num+=1