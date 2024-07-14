def solution(numbers):
    answer = 0
    for i in range(len(numbers) - 1):
        for j in range (i+1, len(numbers)):
            mul = numbers[i] * numbers[j]
            if answer < mul:
                answer = mul 
    return answer