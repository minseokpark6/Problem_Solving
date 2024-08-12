def solution(str_list, ex):
    result = []
    answer = []
    for str in str_list:
        if ex not in str:
            result.append(str)
    answer = "".join(result)
    return answer