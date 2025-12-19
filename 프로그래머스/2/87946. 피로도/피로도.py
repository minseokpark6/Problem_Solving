def solution(k, dungeons):
    # 변수 정의
    n = len(dungeons)
    visited = [False] * n
    max_cnt = 0
    
    # dfs + 백트래킹 함수 정의 
    def dfs(fatigue, cnt):
        nonlocal max_cnt
        max_cnt = max(max_cnt, cnt)
         
        for i in range(n):
            if not visited[i] and fatigue >= dungeons[i][0]:
                visited[i] = True   # 경로 설정
                dfs(fatigue - dungeons[i][1], cnt+1)    # 해당 경로의 다음 뎁스 탐색
                visited[i] = False  # 선택 취소(백트래킹)
                
    # 탐험 가능한 던전 수 카운트
    dfs(k, 0)
    
    # 출력
    return max_cnt

'''
## 개선점 

모든 경우의 수 탐색 vs 깊이 우선 탐색(DFS) + 백트래킹

(1) 불필요한 경우까지 전부 생성 (모든 경우 탐색)
- 이미 피로도가 부족해서 돌지 못하는 경우에도 끝까지 순열을 다 순회 

(2) 상태 재사용이 안됨
- 같은 피로도 상태, 같은 방문 결과를 재사용하지 않고 매번 새 순열로 새로 계산

(3) 시간 복잡도 


## 전역 변수 vs nonlocal 변수의 차이점 
- global : "파일 전체에 공유되는 변수"를 쓰는 것
- nonlocal : "바로 바깥에 있는 함수(enclosing scope)에 있는 변수"를 쓰는 것 

-> 함수 재사용이 안전하고 와부 오염이 없어서 여러 테스트 케이스에서도 안전



## 이전 통과 코드

from itertools import permutations 

def solution(k, dungeons):
    # 변수 정의
    max_cnt = 0
    
    # 순열을 통해 최대 탐험 던전 수 구하기 
    for dungeon in permutations(dungeons):
        # 변수 정의 
        cnt, fatigue = 0, k
        
        # 해당 순서로 탐험 횟수 카운트 
        for i, j in dungeon:
            if fatigue >= i:
                fatigue -= j
                cnt += 1
        
        # 최대 탐험 횟수와 비교 
        if max_cnt < cnt:
            max_cnt = cnt
    
    # 출력
    return max_cnt
    
'''