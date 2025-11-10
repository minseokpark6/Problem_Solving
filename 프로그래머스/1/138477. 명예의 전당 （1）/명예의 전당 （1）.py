def solution(k, score):
    # 변수 정의 
    answer = []
    hall_of_fame = []

    # 발표 점수 담기 
    for s in score:
        # 명예의 전당에 점수 추가
        hall_of_fame.append(s)
        hall_of_fame.sort(reverse=True)
        
        if len(hall_of_fame)>k:
           hall_of_fame.pop()
        
        # 발표 점수 추가 
        answer.append(hall_of_fame[-1])

    # 출력 
    return answer

'''
### heapq 자료구조 사용 ver.

import heapq 

def solution(k, score):
    # 변수 지정 
    result = []
    hall_of_fame = []
    
    # 발표된 최하위 점수 구하기 
    for s in score:
        if len(hall_of_fame) < k:
            heapq.heappush(hall_of_fame, s)
        else:
            # s가 현재 최소값보다 작으면 교체
            if s > hall_of_fame[0]:
                heapq.heappushpop(hall_of_fame, s)
        # 최하위 점수 추가 
        result.append(hall_of_fame[0])
    
    # 출력 
    return result

### heap 자료 구조 사용 
- heapq는 리스트(list)를 힙 자료구조로 취급합니다.
- 힙의 성질: heap[0]에는 항상 가장 작은 값(최소값) 이 위치합니다.
- 내부적으로는 이진 트리(완전이진트리)를 배열로 표현한 구조입니다.
- 힙은 삽입/삭제(루트) 연산이 O(log n) 입니다.

'''