def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]




"""
# 주어진 순서가 바뀜... >> 틀림 

def solution(arr):
    result = sorted(arr)[::-1][:-1]
    if len(result) > 0:
        pass
    elif len(result) == 0:
        result.append(-1)
    return result
"""