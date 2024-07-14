def solution(numbers):
    answer = 0
    li = []
    for idx1 in range(len(numbers)-1):
        for idx2 in range(idx1+1, len(numbers)):
            mul = numbers[idx1] * numbers[idx2]
            li.append(mul)
    answer = max(li)
    return answer