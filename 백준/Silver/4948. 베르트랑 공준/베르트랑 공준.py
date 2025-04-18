import sys
input = sys.stdin.readline

# 1. 입력 최대값 설정
MAX = 246_912

# 2. 에라토스테네스의 체
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

# 3. 입력에 따른 출력
while True:
    n = int(input())
    if n == 0:
        break
    # 소수 개수 출력
    print(sum(is_prime[n+1 : 2*n+1]))