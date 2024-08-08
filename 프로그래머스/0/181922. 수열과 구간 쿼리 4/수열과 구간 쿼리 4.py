def solution(arr, queries):
    for q in queries:
        s, e, k = q[0], q[1], q[2]
        idx_list = list(range(s, e+1))
        for idx in idx_list:
            if idx % k == 0:
                arr[idx] += 1
    return arr