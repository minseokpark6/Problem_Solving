def solution(absolutes, signs):
    result = []
    for idx, n in enumerate(absolutes):
        if signs[idx] == True:
            result.append(n)
        else:
            result.append(-n)
    answer = sum(result)
    return answer