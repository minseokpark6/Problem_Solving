def solution(arr): 
    # 변수 정의
    m = min(arr) 
    # 출력 
    return [i for i in arr if i != m] if len(arr) != 1 else [-1]

'''
## 기존 코드 
def solution(arr):
    if len(arr) == 1:
        return [-1]
    m = min(arr)
    return [x for x in arr if x != m]



## 기존 코드 
>> remove를 사용할 경우 원본 자체를 바꿔버림으로 비추천 

def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]
'''