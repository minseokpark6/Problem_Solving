def solution(numbers):
    # 리스트 내림차순 정렬 
    arr = sorted(numbers, reverse= True)
    # 최대값 출력 
    return arr[0] * arr[1]

'''
def solution(numbers):
    answer = 0
    for i in range(len(numbers) - 1):
        for j in range (i+1, len(numbers)):
            mul = numbers[i] * numbers[j]
            if answer < mul:
                answer = mul 
    return answer
'''