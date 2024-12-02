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


"""
stack 사용하여 재료 순서대로 확인

"""