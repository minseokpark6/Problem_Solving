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