def solution(my_strings, parts):
    result = []
    for idx, part in enumerate(parts):
        s, e = part[0], part[1]
        my_str = my_strings[idx][s:e+1]
        result.append(my_str)
    answer = "".join(result)
    return answer