def solution(k, tangerine): 
    # 빈 딕셔너리 생성
    tan_dic = {}

    # 귤 크기 별 개수 카운트
    for t in tangerine:
        if t in tan_dic.keys():
            tan_dic[t] += 1
        else:
            tan_dic[t] = 1

    # 크기 별 내림차순 정렬 
    sorted_dic = sorted(tan_dic.items(), key=lambda x: (-x[1], x[0]))

    # 서로 다른 종류가 최소일 경우의 수 카운트 
    cnt, total = 0, 0 

    for _, c in sorted_dic:
        total += c
        cnt += 1
        if total >= k:
            break

    # 출력
    return cnt

'''

## 이전 통과 코드 

1. numpy 활용 

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


(1)
리스트에서는 unique 사용할 수 없음 
so. numpy에서 사용 가능 

(1-1)
name, count = np.unique(tangerine, return_counts=True)
Numpy에서 unique 사용 시, return_counts를 사용하면, 
pandas에서 unique, nunique를 동시에 사용하듯 변수를 지정할 수 있음 

2. Counter 활용 

from collections import Counter

def solution(k, tangerine):
    # 귤 크기별 개수 카운트
    tan_count = Counter(tangerine)

    # 개수 기준 내림차순, 크기 기준 오름차순 정렬
    sorted_tan = sorted(tan_count.items(), key=lambda x: (-x[1], x[0]))

    total, cnt = 0, 0

    # 가장 많은 종류부터 차례로 담기
    for _, c in sorted_tan:
        total += c
        cnt += 1
        if total >= k:
            break

    return cnt


'''