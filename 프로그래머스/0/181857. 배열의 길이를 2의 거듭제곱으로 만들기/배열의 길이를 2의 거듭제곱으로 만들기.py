def solution(arr):
    # 2 ** 10 = 1024 // arr의 최대 길이 1,000
    i = 0
    while i < 11:
        if len(arr) == 2**i:
            answer = arr
            break
        elif len(arr) < 2**i:
            n = 2**i - len(arr)
            answer = arr + ([0] * n)
            break
        else:
            i += 1
    return answer

