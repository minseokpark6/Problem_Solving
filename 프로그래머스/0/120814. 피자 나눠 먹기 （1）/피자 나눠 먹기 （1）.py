def solution(n):
    return n//7 if n%7==0 else n//7+1

'''
def solution(n):
    if n <= 7 : 
        answer = 1
    elif n % 7 == 0:
        answer = n // 7
    else:
        answer = (n // 7) + 1
    return answer
'''