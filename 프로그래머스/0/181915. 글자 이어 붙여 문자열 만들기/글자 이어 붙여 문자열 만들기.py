def solution(my_string, index_list):
    result = [my_string[idx] for idx in index_list]
    answer = "".join(result)
    return answer