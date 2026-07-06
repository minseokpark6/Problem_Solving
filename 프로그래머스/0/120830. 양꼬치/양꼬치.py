def solution(n, k):
    l, b = 12000, 2000
    return n*l + k*b - (n//10 * b)


'''
def solution(n, k):
    answer = n*12000 + k*2000 - (n // 10) * 2000
    return answer

'''