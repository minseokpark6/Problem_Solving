def solution(arr):
    answer = []
    
    # 인덱스 담기
    idx_list = []
    for idx, n in enumerate(arr):
        if n == 2:
            idx_list.append(idx)
            
    # 배열 안의 2가 모두 포함된 가장 작은 연속된 배열 구하기
    if len(idx_list) > 1:
        s, e = idx_list[0], idx_list[-1]
        answer = arr[s:e+1]
    elif len(idx_list) == 1:
        answer.append(arr[idx_list[0]])
    else:
        answer.append(-1)
        
    # 출력
    return answer