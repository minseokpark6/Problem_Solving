def solution(score):
    result = []
    # 평균 점수를 담은 리스트 생성
    for i in score:
        avg = sum(i) / len(i)
        result.append(avg)
        
    # 평균 점수를 내림차순으로 정렬
    sorted_result = sorted(result, reverse=True)
    
    # 순위 매기기
    answer = [sorted_result.index(i) + 1 for i in result]
    # 어짜피 겹치는 수는 맨 처음 인덱스를 반환하기 때문에 동점자 처리 가능 
    
    return answer
