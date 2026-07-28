def solution(arr):
    # 변수 정의 
    result = []
    
    # 원소의 개수대로 이어 붙이기 
    for i in arr:
        result += [i]*i
    
    # 출력
    return result


'''
def solution(arr):
    answer = []
    for n in arr:
        for i in range(n):
            answer.append(n)
    return answer
'''