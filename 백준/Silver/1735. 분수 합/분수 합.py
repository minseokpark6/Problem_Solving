import math

# 입력
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

# 분모 통일 및 분자 계산
lcm = math.lcm(a2, b2)
numer = a1 * (lcm // a2) + b1 * (lcm // b2)

# 기약분수로 만들기
gcd = math.gcd(numer, lcm)
print(numer // gcd, lcm // gcd)
