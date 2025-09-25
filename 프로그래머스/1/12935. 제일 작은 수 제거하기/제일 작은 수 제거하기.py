def solution(arr):
    # 배열의 길이가 1인 경우 
    if len(arr) == 1:
        return [-1]
    # 그 외의 경우 
    m = min(arr)
    # 출력
    return [i for i in arr if i != m]

'''
기존 코드 
>> remove를 사용할 경우 원본 자체를 바꿔버림으로 비추천 

def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]
'''