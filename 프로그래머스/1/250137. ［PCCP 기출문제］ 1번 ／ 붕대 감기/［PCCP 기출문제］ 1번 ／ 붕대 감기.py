def solution(bandage, health, attacks):

    # 변수 정의 
    hp = health # 현재 체력
    t, x, y = bandage[0], bandage[1], bandage[2]
    cnt = 0     # 연속 성공 횟수 카운트
    n = attacks[-1][0]  # 총 공격 시간 정의
    idx = 0     # attacks 리스트의 인덱스

    # 몬스터 공격에 따른 체력 증감
    for i in range(1, n+1):
        # 몬스터가 공격한 경우
        if i == attacks[idx][0]:
            hp -= attacks[idx][1]
            idx += 1 
            cnt = 0     # 연속 공격 초기화
            # hp가 0이 된 경우 
            if hp <= 0:
                hp = -1
                break
        
        # 몬스터가 공격하지 않은 경우 
        else:
            hp += x
            cnt += 1
            # 연속 성공 횟수 달성 시 
            if cnt == t:
                hp += y
                cnt = 0
            # 체력이 최대 체력을 초과한 경우 
            if hp > health:
                hp = health
                        
    return hp