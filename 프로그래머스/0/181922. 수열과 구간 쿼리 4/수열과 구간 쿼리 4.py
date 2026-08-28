def solution(arr, queries):
    # arr 변환하기 
    for q in queries:
        idx_list = list(range(q[0], q[1]+1))
        for idx in idx_list:
            if idx % q[2] == 0:
                arr[idx] += 1
    
    # 출력
    return arr
                


'''

def solution(arr, queries):
    for q in queries:
        s, e, k = q[0], q[1], q[2]
        idx_list = list(range(s, e+1))
        for idx in idx_list:
            if idx % k == 0:
                arr[idx] += 1
    return arr
'''