def solution(n):
    return sum(i for i in range(1, n+1, 2)) if n%2 == 1 else sum(i**2 for i in range(2, n+1, 2))


'''
def solution(n):
    answer = 0
    if n % 2 != 0:
        for i in range(1, n+1, 2):
            answer += i
    else:
        for i in range(2, n+1, 2):
            answer += (i ** 2)

    return answer
'''
            