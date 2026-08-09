def solution(my_string):
    return sorted(my_string[idx:] for idx in range(len(my_string)))

'''
def solution(my_string):
    result = [my_string[i:] for i in range(len(my_string))]
    answer = sorted(result)
    return answer
'''