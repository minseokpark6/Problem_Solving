def solution(str_list):
    answer = []
    for idx, s in enumerate(str_list):
        if s == "l":
            answer = str_list[:idx]
            break
        elif s == "r":
            answer = str_list[idx+1:]
            break
        else:
            pass
    return answer