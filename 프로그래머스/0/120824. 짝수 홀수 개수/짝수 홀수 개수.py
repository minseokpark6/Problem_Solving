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