def solution(num_list):
    result = []
    for idx, num in enumerate(num_list):
        if num < 0:
            result.append(idx)
    if len(result) == 0:
        return -1
    elif len(result) >= 1:
        return result[0]