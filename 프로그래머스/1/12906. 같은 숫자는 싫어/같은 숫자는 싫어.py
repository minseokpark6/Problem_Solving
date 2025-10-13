def solution(arr):
    # 스택 생성 
    stack = []
    # 연속되지 않은 숫자만 스택에 추가
    for i in arr:
        # 스택이 비어있거나 숫자가 다른 경우에만 스택에 추가
        if not stack or i != stack[-1]:
            stack.append(i)
    # 출력
    return stack

'''
이전 통과 코드
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
    '''