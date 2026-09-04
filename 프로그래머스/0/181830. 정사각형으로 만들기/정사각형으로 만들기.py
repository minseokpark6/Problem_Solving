def solution(arr):
    # 변수 정의 
    x, y = len(arr[0]), len(arr)

    # 이차원 배열에 0 추가 후 출력
    if x < y:
        return [i + [0]*(y-x) for i in arr]
    elif x > y:
        return arr + [[0] * x] * (x - y)
    else:
        return arr



'''
def solution(arr):
    # 이차원 리스트의 (x, y)값 비교
    for i in range(len(arr)):
        # y값이 클 경우 > 2차원 리스트 원소인 1차원 리스트에 0값 추가
        if len(arr) > len(arr[i]):
            arr[i] = arr[i] + ([0] * (len(arr) - len(arr[i])))
            
        # x값이 클 경우 > 2차원 리스트 원소인 1차원 리스트의 len값 만큼 0으로 이루어진 리스트 추가
        elif len(arr) < len(arr[i]):
            arr = arr + [[0] * len(arr[i])] * (len(arr[i]) - len(arr))
             
    return arr
'''