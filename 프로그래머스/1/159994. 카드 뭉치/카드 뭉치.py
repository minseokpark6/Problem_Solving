from collections import deque

def solution(cards1, cards2, goal):
    # 변수 지정 
    q1 = deque(cards1)
    q2 = deque(cards2)
    
    # 가능 여부 확인
    for w in goal:
        if q1 and q1[0] == w:
            q1.popleft()
        elif q2 and q2[0] == w:
            q2.popleft()
        else:
            return 'No'
    
    # 출력
    return 'Yes'


''' 

## 이전 통과 코드 

def solution(cards1, cards2, goal):
    # 변수 지정 
    l1, l2 = len(cards1), len(cards2)
    idx1, idx2 = 0, 0
    
    # 가능 여부 확인
    for w in goal:
        if (l1 > idx1) and (cards1[idx1] == w):
            idx1 += 1
        elif (l2 > idx2) and (cards2[idx2] == w):
            idx2 += 1
        else:
            return 'No' 
    
    # 출력 
    return 'Yes'
'''