def solution(name, yearning, photo):
    # 변수 지정 
    answer = []
    dic = {i:j for i, j in zip(name, yearning)}
    
    # 그리움 점수 합산 
    for p in photo:
        score = 0
        for n in p:
            if n in name:
                score += dic[n]
        answer.append(score)

    # 출력
    return answer