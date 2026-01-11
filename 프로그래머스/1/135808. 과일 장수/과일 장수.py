def solution(k, m, score):
    # score 정렬
    score.sort(reverse = True)
    
    # 최대 이익 출력
    return sum(score[i]*m for i in range(m-1, len(score), m))


'''
## 기존 통과 코드
def solution(k, m, score):
    # 변수 설정 
    answer = 0

    # 내름차순 정렬 
    score.sort(reverse=True)

    # 박스 별 점수 카운트 
    # >> 내림차순 정렬로 m번째 마다 최소값 자리에 해당
    for i in range(m-1, len(score), m):
        answer += score[i]*m

    # 출력
    return answer



>> 기존 코드 대비 개선점
1) min() 호출로 인한 O(m) -> O(1)로 최적화 
2) 슬라이싱 제거 


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


'''