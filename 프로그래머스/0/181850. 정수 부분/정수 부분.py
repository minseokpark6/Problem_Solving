def solution(flo):
    answer = int(flo)
    return answer

'''
(1)
반올림: round 

(2)
버림: int >> 실수에서 소수점 이하를 버리고 정수 데이터로 변경 

(3)

올림
1. math 모듈 활용 
import math
math.ceil(flo)

2. 올림은 소수점이 있는 경우, 정수에 +1을 하면 되기 때문에 

if flo > int(flo):
    answer = int(flo) + 1
else: 
    answer = int(flo)

'''