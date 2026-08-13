def solution(arr):
    # 변수 정의 
    n = len(arr)
    
    # 조건 확인
    for i in range(n):
        for j in range(i+1, n):
            if arr[i][j] != arr[j][i]:
                return 0
    # 출력
    return 1
    
'''
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
            else:
                pass
    return 1
'''