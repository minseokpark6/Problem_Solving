def solution(k, score):
    # 변수 지정
    answer = []
    hall_of_fame = []
    
    # 발표 점수 확인
    for i in score:
        hall_of_fame.append(i)
        hall_of_fame.sort(reverse=True)
        if len(hall_of_fame) <= k:
            answer.append(hall_of_fame[-1])
        else:
            hall_of_fame.pop()
            answer.append(hall_of_fame[-1])
            
    # 출력
    return answer