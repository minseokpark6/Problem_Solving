import math 
t = int(input())
# 다리를 놓을 수 있는 경우의 수 출력 
for _ in range(t):
    n, m = map(int, input().split())
    cnt = int(math.factorial(m) / (math.factorial(n) * math.factorial(m-n)))
    print(cnt)