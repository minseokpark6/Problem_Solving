def solution(arr, divisor):
    # divisor로 나누어 떨어지는 값 구하기
    answer = sorted([i for i in arr if i % divisor == 0])
    # 출력
    return answer if answer else [-1]


''' 이전 코드
def solution(arr, divisor):
    answer = []
    # arr의 원소 중 divisor로 나뉘어지는 수 선별
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    # answer이 비어있을 경우, -1 추가     
    if len(answer) > 0:
        answer.sort()
    else:
        answer.append(-1)
    # 출력
    return answer
'''