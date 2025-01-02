def solution(d, budget):
    # 변수 정의
    answer = 0
    
    # 예산 범위 내 지원 가능한 부서 찾기 
    for i in sorted(d):
        if i <= budget:
            answer += 1
            budget -= i
        
    # 출력           
    return answer


