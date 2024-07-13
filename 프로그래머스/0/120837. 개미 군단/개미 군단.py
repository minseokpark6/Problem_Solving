def solution(hp):
    answer = 0
    # 장군 개미 수
    j = hp // 5
    # 남은 HP 
    hp = hp % 5
    # 개미 수 합산
    answer += j
    
    # 병정 개미 수 
    b = hp // 3
    # 남은 HP 
    hp = hp % 3
    # 개미 수 합산
    answer += b
    
    # 일 개미 수 
    i = hp // 1
    # 개미 수 합산 
    answer += i    
    
    return answer