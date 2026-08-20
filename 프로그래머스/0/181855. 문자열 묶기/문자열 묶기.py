def solution(strArr):
    # 변수 정의 
    length = {}
    
    # 길이가 같은 문자열 개수 카운트
    for s in strArr:
        l = len(s)
        if l in length:
            length[l] += 1
        else:
            length[l] = 1
            
    # 개수가 가장 많은 그룹의 크기 출력
    return sorted(length.values())[-1]


'''
## 이전 정답 코드 
from collections import Counter

def solution(strArr):
    length = [len(s) for s in strArr]
    result = Counter(length)
    answer = sorted(list(result.values()))[-1]
    return answer

Pandas df에서의 value_count() >> list : Counter()

1) 
result = Counter(length)
result

>> Counter({1: 2, 2: 2, 3: 1})

2)
type((result))
>> collections.Counter

3) 
list(result.values())
>> [2, 2, 1]

'''
