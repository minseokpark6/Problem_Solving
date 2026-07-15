def solution(n):
    return sum(map(int, str(n)))

'''

def solution(n):
    answer = 0
    for i in range(len(str(n))):
        answer += int(str(n)[i])
    return answer
'''