def solution(arr, queries):
    # 순서대로 배열 값 변경 
    for q in queries:
        i, j = q[0], q[1]
        arr[i], arr[j] = arr[j], arr[i]
    
    # 출력
    return arr