from copy import deepcopy
def solution(emergency):
    # 정답 받을 리스트 생성
    answer = [0] * len(emergency)
    
    # 리스트 복사
    copied = deepcopy(emergency)
    # 응급도 순서대로 정렬
    copied = sorted(copied, reverse = True)

    # 응급도 순서대로 인덱스 붙이기 
    for i in copied:
        rank = copied.index(i) + 1
        origin_idx = emergency.index(i)

        answer[origin_idx] = rank

    return answer