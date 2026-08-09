def solution(n, k):
    return list(range(k, n+1, k))

'''
def solution(n, k):
    answer = []
    arr = list(range(1, n+1))
    for num in arr:
        if num % k == 0:
            answer.append(num)
    return answer
'''