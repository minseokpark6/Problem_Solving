import math

def solution(n):
    # 변수 정의 
    cnt = 0
    root = math.isqrt(n)
    # 순서쌍 개수 => 약수의 개수 카운트 
    for i in range(1, root+1):
        if i ** 2 ==n:
            cnt += 1
        elif n % i ==0:
            cnt += 2
    # 출력
    return cnt

'''
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    return answer
'''