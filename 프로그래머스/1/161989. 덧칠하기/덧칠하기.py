def solution(n, m , section):
    # 변수 정의 
    result = 0
    painted_end = 0
    
    # 페인트 칠 횟수 카운트 
    for s in section:
        if s > painted_end:
            result += 1
            painted_end = s + (m-1)
    
    # 출력
    return result

'''
## 개선점
- 문제 풀이 접근 방식은 동일, 가독성을 좀 더 직관적인 방식으로 변경


## 이전 통과 코드 

def solution(n, m, section):
    # 변수 정의: 무조건 페인트칠을 한 번은 해야함 
    cnt = 1
    # 페인트칠의 기준이 되는 구역 설정
    std = section[0]
    
    # 페인트칠 횟수 카운트 
    for s in section:
        if std + (m-1) < s:
            std = s
            cnt += 1
    
    # 출력
    return cnt
    
'''