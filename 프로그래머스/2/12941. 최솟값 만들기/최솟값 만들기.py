def solution(A,B):
    # 리스트 컴프리헨션으로 변경
    answer = sum([i*j for i, j in zip(sorted(A), sorted(B, reverse = True))])
    # 출력
    return answer

""" 
>> 시간 초과 

def solution(A,B):
    answer = 0
    # A 리스트에서 가장 작은 수를 B 리스트에서 가장 큰 수와 곱해서 더하는 것이 최소값
    while True:
        min_num_A, max_num_B = min(A), max(B)
        answer += (min_num_A * max_num_B)
        A.remove(min_num_A)
        B.remove(max_num_B)
        # 정지 조건 
        if len(A) == 0:
            break
    # 출력
    return answer
"""