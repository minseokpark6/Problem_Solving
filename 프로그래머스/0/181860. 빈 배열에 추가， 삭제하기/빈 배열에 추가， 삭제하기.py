def solution(arr, flag):
    # 변수 정의 
    result = []
    
    # X에 원소 추가하기 
    for idx, i in enumerate(arr):
        if flag[idx]:
            result.extend([i]*i*2)
        else:
            result = result[:-i]
    
    # 출력
    return result

'''
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
'''