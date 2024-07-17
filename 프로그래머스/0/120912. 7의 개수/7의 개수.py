def solution(array):
    answer = 0
    array = [str(num) for num in array]
    for num in array:
        for i in num:
            if i == '7':
                answer += 1
    return answer