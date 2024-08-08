def solution(arr, queries):
    answer = []
    # s, e, k 값 정의
    for q in queries:
        temp = []
        s, e, k = q[0], q[1], q[2]
        # k보다 큰 arr[i]값 temp에 담기
        for a in arr[s:e+1]:
            if a > k:
                temp.append(a)
        # temp 리스트에서 가장 작은 arr[i]값 찾기
        if len(temp) >= 1:
            result = sorted(temp)[0]
        else:
            result = -1
        # answer 리스트에 담기
        answer.append(result)
    
    return answer