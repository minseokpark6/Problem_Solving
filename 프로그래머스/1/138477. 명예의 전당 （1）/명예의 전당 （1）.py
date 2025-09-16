def solution(k, score): 
    # 변수 지정 
    result = []
    hall_of_fame = []

    # 발표된 최하위 점수 구하기 
    for s in score:
        # 명예의 전당에 점수 추가
        if len(hall_of_fame) >= k:
            if hall_of_fame[-1] < s:
                hall_of_fame.pop()
                hall_of_fame.append(s)
        else:
            hall_of_fame.append(s)
        
        # 최하위 점수 발표 
        hall_of_fame.sort(reverse=True)
        result.append(hall_of_fame[-1])

    # 출력
    return result