def solution(my_string, n):
    answer = ''
    for idx in range(len(my_string)):
        answer += (my_string[idx] * n)
    return answer