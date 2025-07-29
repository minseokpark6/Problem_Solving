def solution(schedules, timelogs, startday):
    # 변수 정의
    answer = 0
    n = len(schedules)

    # 주말 출근 기록 삭제 
    for time in timelogs:
        if startday == 7:
            time.pop()
            time.pop(0)
        else:
            time.pop(7-startday-1)
            time.pop(7-startday-1)

    for i in range(n):
        cnt = 0
    
        # 출근 인정 시간 변수 지정
        h = schedules[i] // 100
        m = schedules[i] % 100
        if m >= 50:
            h += 1
            m -= 50
            scheduled = h*100 + m
        else:
            scheduled = schedules[i] + 10
            
        # 평일 출근 시간 확인
        for j in range(5):
            if timelogs[i][j] <= scheduled:
                cnt += 1
            else:
                break

        # 상품 수령할 직원 카운트
        if cnt == 5:
            answer += 1

    # 출력
    return answer