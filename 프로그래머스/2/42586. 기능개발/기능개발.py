def solution(progresses, speeds):
    # 변수 지정
    answer = []
    days = []
    
    # 각 작업 별 완료 일 설정
    for idx, pro in enumerate(progresses):
        d = 0
        while pro < 100:
            pro += speeds[idx]
            d += 1
        days.append(d)
    
    # 배포일 별 기능 개수 카운트
    release = days[0]
    count = 1
    
    for day in days[1:]:
        if release >= day:
            count += 1
        else:
            answer.append(count)
            release = day
            count = 1
            
    answer.append(count)
    
    # 출력 
    return answer