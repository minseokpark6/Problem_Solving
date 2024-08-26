def solution(arr):
    answer = []
    # arr의 첫번째 원소값 추가
    answer.append(arr[0])
    # 연속되지 않은 원소만 추가
    for idx in range(1, len(arr)):
        if arr[idx] != arr[idx-1]:
            answer.append(arr[idx])
    # 출력
    return answer