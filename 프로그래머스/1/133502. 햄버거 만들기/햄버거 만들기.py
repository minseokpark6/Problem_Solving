from collections import deque

def solution(ingredient):
    # 변수 지정 
    cnt = 0 
    stack = deque()

    # 재료의 경우의 수 확인
    for i in ingredient:
        stack.append(i)
    
        # 햄버거를 만들 수 있는 경우의 수인지 확인
        if i == 1 and len(stack) >= 4:
            if stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
                cnt += 1
                for i in range(4):
                    stack.pop()

    # 출력
    return cnt

"""
1) deque를 활용하여 삽입/삭제 안정적으로 O(1), 대량 데이터에 성능개선 
    -> 슬라이싱은 불가능
'''


''' 이전 코드
def solution(ingredient):
    # 변수 지정
    answer = 0
    stack = []
    
    # 재료가 순서대로 나오는 경우의 수 확인 
    for i in ingredient:
        stack.append(i)
        if i == 1 and len(stack) >= 4:
            if stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
                answer += 1
                for i in range(4):
                    stack.pop()
    # 출력
    return answer

>>>
stack 사용하여 재료 순서대로 확인
"""