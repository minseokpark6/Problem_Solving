import math
# 입력
n, k = map(int, input().split())
# 출력
print(int(math.factorial(n)/(math.factorial(n-k)*math.factorial(k))))