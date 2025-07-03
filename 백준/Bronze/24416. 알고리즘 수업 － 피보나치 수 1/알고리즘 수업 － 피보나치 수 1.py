# 입력 
n = int(input())

# 재귀함수 카운트 
# 재귀 함수의 호출 횟수가 피보나치 수를 따름 >> 동적 계획법으로 연산 시간 보완 가능
def recursion_cnt(n):
    prev, cur = 1, 1  # prev=F(i-2), cur=F(i-1)
    for _ in range(3, n + 1):
        prev, cur = cur, prev + cur  # F(i) = F(i-1)+F(i-2)
    return cur        # cur == F(n)

# 동적 계획법 카운트
# >> 0과 1을 제외하고 n만큼 함수가 돌아가기 때문
# n이 5 이상이기 때문에 0과 1의 경우 생각하지 않아도 됨
def dynamic_cnt(n):
    return n-2

print(recursion_cnt(n), dynamic_cnt(n))


'''
# 재귀함수를 활용한 피보나치수 함수
def recursion(n):
    if n >= 2:
        return recursion(n-2) + recursion(n-1)
    else:
        return n

# 동적 계획법을 활용한 피보나치 수 함수
f = [0] * (n+1)
def dynamic(n):
    f[1] = 1 
    f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
'''