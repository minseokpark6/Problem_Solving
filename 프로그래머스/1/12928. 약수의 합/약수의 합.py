def solution(n):
    return sum([i for i in range(1, n+1) if n%i == 0])


''' 이전 코드
def solution(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    answer = sum(result)
    return answer
'''