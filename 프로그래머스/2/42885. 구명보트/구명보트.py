def solution(people, limit):
    # 변수 정의 
    cnt = 0
    first, last = 0, len(people)-1
    
    # 몸무게 내림 차순 정리 
    people.sort(reverse=True)
    
    # 보트의 최소값 구하기 
    while first <= last:
        
        # 가장 가벼운 사람과 무거운 사람을 함께 태울 수 있는 경우
        if people[first]+people[last] <= limit:
            # 무거운 사람과 함께 보트에 탑승
            last -= 1
        
        # 구명정 개수 추가, 무거운 사람 보트에 탑승 후 인덱스 이동 
        cnt += 1
        first += 1
    
    # 출력
    return cnt

'''

## 탐욕법(Greedy Algorithm)이란?
현재 시점에서 가장 최선(최적) 으로 보이는 선택을 반복해서,
전체적으로도 최적해(또는 근사 최적해)에 도달하려는 알고리즘 설계 방법


## 탐욕법의 핵심 아이디어
1. 매 순간의 선택이 전체에서도 최적일 것이라는 가정
2. 이미 한 선택은 다시 번복하지 않는다 (비가역적)

## 단점 
항상 정답을 보장하진 않음  -> 특정 문제에서만 유효

'''

