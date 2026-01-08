from collections import deque

def solution(priorities, location):
    # 변수 정의
    q = deque([(i, p) for i, p in enumerate(priorities)])
    sorted_pr = sorted(priorities, reverse=True)
    
    answer = 0
    
    # 실행 순서 추적
    while q:
        idx, priority = q.popleft()
        
        if priority == sorted_pr[0]:
            answer += 1
            sorted_pr.pop(0)

            if idx == location:
                return answer
        
        else:
            q.append((idx, priority))
'''
## 개선점
(1) 시간 복잡도 개선
- deque 메소드를 활용하여 remove or pop 최소 사용


## 이전 통과 코드 

def solution(priorities, location):
    # 변수 설정
    order = 0 
    # 우선 순위와 로케이션 설정 
    pr = [[idx, i] for idx, i in enumerate(priorities)]
    # priorities 내림차순 정렬 
    sorted_pr = sorted(priorities, reverse=True)
    
    # 실행순서 찾기 
    while pr:
        temp = pr[0]
        pr.pop(0)
        # 가장 우선순위가 높은 수 설정 
        first = sorted_pr[0]
        
        if temp[1] != first:
            pr.append(temp)
            
        elif temp[1] == first:
            # location 확인
            if temp[0] == location:
                order += 1
                break
            else:
                sorted_pr.pop(0)
                order += 1
    
    # 출력
    return order
            
'''