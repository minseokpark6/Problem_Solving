def solution(money):
    return [money // 5500, money%5500]

'''

def solution(money):
    answer = []
    n = money // 5500
    answer.append(n)
    r = money - (5500*n)
    answer.append(r)
    return answer
'''