def solution(rank, attendance):
    result = []
    
    # attendance가 True인 값만 리스트에 담기
    for idx, r in enumerate(rank):
        if attendance[idx] == True:
            result.append(r)
            
    # rank 순 정렬
    result = sorted(result)
    
    # 인덱스값 추출 후 answer 출력
    answer = 10000 * (rank.index(result[0])) + 100 * (rank.index(result[1])) + (rank.index(result[2])) 
    
    # 출력
    return answer