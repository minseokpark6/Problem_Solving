def solution(my_string):
    result = my_string.strip(" ").split(" ")
    answer = []
    for s in result:
        if s != '':
            answer.append(s)
    return answer