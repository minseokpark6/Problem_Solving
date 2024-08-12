def solution(arr, flag):
    answer = []
    for idx, num in enumerate(arr):
        if flag[idx] == True:
            for i in range(num*2):
                answer.append(num)
        else:
            for i in range(num):
                answer.pop()
    return answer