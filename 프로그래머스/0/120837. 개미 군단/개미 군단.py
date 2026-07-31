def solution(hp):
    # 변수 정의
    attack = [5, 3, 1]
    cnt = 0
    # 사냥감의 체력에 맞는 최소한의 병력 구하기
    for i in attack:
        cnt += (hp//i)
        hp %= i

        if hp == 0:
            return cnt                  

'''
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
'''