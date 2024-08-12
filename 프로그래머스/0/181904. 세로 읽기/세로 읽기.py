def solution(my_string, m, c):
    answer = ''
    for idx in range(c-1, len(my_string), m):
        answer += my_string[idx]
    return answer