def solution(n, lost, reserve):
    # 여벌 체육복이 있는 학생이 체육복을 도난당한 경우 제외
    lost_ = set(lost) - set(reserve)
    reserve_ = set(reserve) - set(lost)
    
    # 변수 지정 
    answer = n - len(lost_)

    # 체육복을 빌려입을 수 있는 학생 추가 카운트
    for i in lost_:
        if i-1 in reserve_:
            answer += 1
            reserve_.remove(i-1)
        elif i+1 in reserve_:
            answer += 1
            reserve_.remove(i+1)
        
    # 출력
    return answer


"""
# 실패 >> 자기가 도난당한 경우 제외하지 않음


def solution(n, lost, reserve):
    # 변수 지정
    answer = n - len(lost)
    
    # 체육복을 빌려입을 수 있는 학생 추가 카운트
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
    
    # 출력
    return answer

"""