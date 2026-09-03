def solution(sides):
    return 2*min(sides) - 1
    
    


'''
## 삼각형 한 변의 개수 
(1) range1 => range(max_side-min_side+1, max_side+1)
- max_side - (max_side-min_side+1) +1 
- (min_side)개

(2) range2 => range(max_side+1, sum_sides)
- (max_side+min_side) - (max_side+1)
 - (min_side - 1) 개
 
 Total: (2*min_side -1)개



## 이전 풀이 코드
def solution(sides):
    # 변수 정의
    max_side, min_side = max(sides), min(sides)
    sum_sides = sum(sides)
    
    # 삼각형 조건에 맞는 변 구하기
    # 1. max_side가 가장 긴 변인 경우 
    arr_1 = list(range(max_side-min_side+1, max_side+1))
    # 2. 그 외의 변이 가장 긴 경우
    arr_2 = list(range(max_side+1, sum_sides))
    
    # 정수의 개수 출력
    return len(set(arr_1 + arr_2))
'''