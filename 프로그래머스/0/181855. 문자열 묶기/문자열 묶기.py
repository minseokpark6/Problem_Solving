from collections import Counter

def solution(strArr):
    length = [len(s) for s in strArr]
    result = Counter(length)
    answer = sorted(list(result.values()))[-1]
    return answer

'''
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
