def solution(number):
    return sum(int(n) for n in number) % 9

'''
def solution(number):
    sum = 0
    for s in number:
        sum += int(s)
    answer = sum % 9
    return answer
'''