def solution(str_list, ex):
    return "".join(s for s in str_list if ex not in s)

'''
def solution(str_list, ex):
    result = []
    answer = []
    for str in str_list:
        if ex not in str:
            result.append(str)
    answer = "".join(result)
    return answer
'''