from itertools import accumulate 

def solution(d, budget):
    return sum(i <= budget for i in accumulate(sorted(d)))

'''
(1) 누적합 메소드를 활용하여 풀이

## 이전 코드 

def solution(d, budget):
    # 변수 정의
    cnt = 0

    # 예산 범위 내에서 최대로 지원가능한 부서의 수
    for i in sorted(d):
        if i <= budget:
            cnt += 1 
            budget -= i 
        else:
            break
        
    # 출력
    return cnt

'''