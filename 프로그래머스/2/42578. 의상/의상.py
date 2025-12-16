from collections import Counter

def solution(clothes):
    # 가지고 있는 옷의 개수 카운트
    clothing = Counter(kind for _, kind in clothes)

    # 조합 경우의 수 카운트 
    cnt = 1
    for c in clothing.values():
        cnt = cnt*(c+1)

    # 출력
    return cnt - 1

'''

## 이전 통과 코드 

def solution(clothes):
    # 옷 종류 별 개수 카운트할 딕셔너리 생성 
    dict = {cloth[1]:0 for cloth in clothes}
    
    # 옷 종류 별 개수 카운트
    for cloth in clothes:
        dict[cloth[1]] += 1
    
    # 경우의 수 카운트
    temp = 1
    for num in dict.values():
        temp = temp *(num + 1)

    return temp - 1
    
## 경우의 수 

- 종류 별로 나올 수 있고, 아예 안나올 수도 있고 -> (+ 1)
- 모든 옷이 없는 1개의 경우 제외 ->  (- 1)
'''