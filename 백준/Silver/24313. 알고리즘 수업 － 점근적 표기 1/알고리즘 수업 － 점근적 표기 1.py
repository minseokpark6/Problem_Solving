import sys 
input = sys.stdin.readline 
# 입력
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input()) 
# 출력 
if (c>a1) and (a0/(c-a1) <= n0):
    print(1)
elif (c==a1) and (a0<0):
    print(1)
else:
    print(0)

'''
# 주어진 함수
n >= n0
f(n) = a1*n + a0
f(n) <= c * n

# 함수 전개
- a1*n + a0 <= c * n
- a0 <= (c-a1)*n

(1) (c-a1)이 양수일 경우 
- a0 값에 상관없이 성립

    - a0 / (c-a1) <= n
    - n0 <= n

    >> a0/(c-a1) <= n0

(2) (c-a1)이 0일 경우 
- a0가 음수일 경우에만 성립

(3) (c-a1)이 음수일 경우
- 성립할 수 없음

'''