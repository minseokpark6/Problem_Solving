def solution(common):
    d1 = common[1] - common[0]
    d2 = common[2] - common[1]
    if d1 == d2:
        answer = common[-1] + d1
    else:
        ratio = d2 / d1
        answer = common[-1] * ratio
    return answer