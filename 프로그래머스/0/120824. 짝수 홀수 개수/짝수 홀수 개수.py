def solution(num_list):
    even, odd = 0, 0
    for i in num_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return [even, odd]

'''
def solution(num_list):
    answer = []
    even = []
    odd = []
    for i in num_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    e = len(even)
    answer.append(e)
    o = len(odd)
    answer.append(o)
    return answer
'''