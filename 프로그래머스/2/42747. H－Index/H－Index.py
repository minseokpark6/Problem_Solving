def solution(citations):
    # 변수 지정
    h = len(citations)
    
    # H-index 찾기
    while True:
        if sum([n >= h for n in citations]) >= h:
            break
        else:
            h -= 1

    # 출력
    return h


'''
# 시간 초과 실패

def solution(citations):
    # 변수 지정 
    idx = len(citations) // 2
    # 내림차순 정렬
    citations.sort(reverse = True)
    
    # H-index 찾기
    while True:
        if len(citations[:idx+1]) == citations[idx]:
            answer = citations[idx]
            break
        elif len(citations[:idx+1]) > citations[idx]:
            idx -= 1
            
        elif len(citations[:idx+1]) < citations[idx]:
            idx += 1

    # 출력
    return answer

'''