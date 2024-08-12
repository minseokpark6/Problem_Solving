def solution(arr, n):
    answer = []
    for idx, num in enumerate(arr):
        if len(arr) % 2 != 0:
            if idx % 2 == 0:
                num += n
            answer.append(num)
        else:
            if idx % 2 != 0:
                num += n
            answer.append(num)      
    return answer