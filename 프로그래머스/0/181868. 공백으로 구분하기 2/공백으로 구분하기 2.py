def solution(my_string):
    return [s for s in my_string.strip().split(" ") if s != ""]
'''
def solution(my_string):
    result = my_string.strip(" ").split(" ")
    answer = []
    for s in result:
        if s != '':
            answer.append(s)
    return answer
'''