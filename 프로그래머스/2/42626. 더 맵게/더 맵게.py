import heapq
def solution(scoville, K):
    # 변수 정의
    answer = 0
    
    # 힙(heap) 자료구조로 변경 
    heapq.heapify(scoville)
    
    
    # K 이상의 스코빌로 만들기 
    while len(scoville) > 1:
        # 가장 작은 수와 그 다음 수 pop
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        
        # 가장 작은 수가 K보다 클 경우 종료 
        if s1 >= K:
            return answer
        
        # heap 자료 구조에 섞은 음식의 스코빌 지수 넣기
        temp = s1 + s2*2
        heapq.heappush(scoville, temp)
        
        # 섞은 횟수 카운트
        answer += 1

    # 출력
    return answer if scoville[0] >= K else -1

"""
## heapq
- 힙(heap) 자료구조를 다루는 모듈
- 힙은 **우선순위 큐(priority queue)**를 구현하기 위해 사용
- 파이썬의 heapq는 **최소 힙(min-heap)**을 기본으로 제공

(1) 특징 
- 최소 힙(min-heap): 힙의 루트(첫 번째 요소)가 항상 가장 작은 값을 가짐
- 정렬 상태 유지: 데이터를 삽입하거나 삭제할 때마다 힙 특성을 유지하도록 자동으로 정렬
- 시간 복잡도: 삽입과 삭제 연산이 O(log n)의 시간 복잡도를 가짐



"""