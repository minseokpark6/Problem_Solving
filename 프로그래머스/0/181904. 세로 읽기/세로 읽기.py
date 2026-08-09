def solution(my_string, m, c):
    return "".join(my_string[idx] for idx in range(c-1, len(my_string), m))

'''
def solution(my_string, m, c):
    answer = ''
    for idx in range(c-1, len(my_string), m):
        answer += my_string[idx]
    return answer
'''