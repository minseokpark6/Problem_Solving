import numpy as np

def solution(k, tangerine):
    # 귤 크기 별 개수 카운트
    name, count = np.unique(tangerine, return_counts=True)
    # count 리스트화 
    count = sorted(list(count), reverse=True)
    
    # 카운트한 개수와 k값 비교
    answer, result = 0, 0
    for c in count:
        if c >= k:
            answer += 1
            break 
        else:
            result += c
            answer += 1
            if k <= result:
                break
    # 출력
    return answer

"""
(1)
리스트에서는 unique 사용할 수 없음 
so. numpy에서 사용 가능 

(1-1)
name, count = np.unique(tangerine, return_counts=True)
Numpy에서 unique 사용 시, return_counts를 사용하면, 
pandas에서 unique, nunique를 동시에 사용하듯 변수를 지정할 수 있음 
"""