def solution(arr, idx):
    answer = -1
    for i, n in enumerate(arr):
        if i < idx:
            pass
        else:
            if n == 1:
                answer = i
                break
            else:
                pass
    return answer