def solution(my_string, is_suffix):
    suffix = [my_string[i:] for i in range(len(my_string))]
    if is_suffix in suffix:
        return 1
    else:
        return 0
    return answer