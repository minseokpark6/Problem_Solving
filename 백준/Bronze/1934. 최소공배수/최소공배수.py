import math 
# 입력 
t = int(input())
# 두 수 입력 및 최소공배수 출력 
for _ in range(t):
    a, b = map(int, input().split())
    print(math.lcm(a, b))