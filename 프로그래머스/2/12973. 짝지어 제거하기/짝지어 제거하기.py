def solution(s):
    # 빈 리스트 생성
    stack = []
    
    # 같은 알파벳 1차 제거 
    for i in s: 
        if not stack:
            stack.append(i)
            continue
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    # 같은 알파벳 2차 제거 
    for idx in range(len(stack)-1):
        if stack[idx] == stack[idx+1]:
            stack.pop(idx)
    
    # 출력
    return 0 if stack else 1