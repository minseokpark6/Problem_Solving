def solution(arr, queries):
    # 구간 쿼리 처리 
    for q in queries:
        for i in range(q[0], q[1]+1):
            arr[i] += 1
    
    # 출력
    return arr

'''
def solution(arr, queries):
    for q in queries:
        s, e = q[0], q[1]
        for i in range(s, e+1):
            arr[i] += 1
    return arr

'''