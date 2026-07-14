import math

def solution(n):
    # 변수 정의 
    root = math.isqrt(n)
    small, large = [], []

    # 약수 구하기 
    for i in range(1, root+1):
        if n%i == 0:
            small.append(i)
            if i != n//i:
                large.append(n//i)

    # 출력
    return small + large[::-1]


'''
## 개선점
- 시간 복잡도 개선
    - 루트를 활용하여 for 반복문 복잡도를 낮췄고, 
    - 리스트 두개를 활용하여 정렬 시간 복잡도를 낮춤

def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0 :
            answer.append(i)
    return answer
'''