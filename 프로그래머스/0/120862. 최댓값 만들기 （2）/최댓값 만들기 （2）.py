def solution(numbers):
    answer = 0
    li = []
    for idx1 in range(len(numbers)-1):
        for idx2 in range(idx1+1, len(numbers)):
            mul = numbers[idx1] * numbers[idx2]
            li.append(mul)
    answer = max(li)
    return answer

'''
def solution(numbers):
    answer = 0
    for idx1 in range(len(numbers)-1):
        for idx2 in range(idx1+1, len(numbers)):
            mul = numbers[idx1] * numbers[idx2]
            if mul > answer :
                answer = mul
    return answer
'''
# 테스트 7 통과 X 
# 모든 mul 값이 음수가 나올 경우도 고려해야함
# 부등호는 음수의 최대값을 표현하기 부적합
