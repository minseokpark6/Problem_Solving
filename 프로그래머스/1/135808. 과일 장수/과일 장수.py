def solution(k, m, score):
    # 변수 설정
    answer = 0
    box_count = len(score) // m
    
    # score 내름차순 정렬 
    score.sort(reverse = True)
    
    # 박스 별 점수 카운트
    for i in range(box_count):
        box = score[i*m:(i+1)*m]
        answer += min(box) * m
    
    # 출력
    return answer