def solution(s):
    # 변수 지정
    answer = 0
    
    # s를 왼쪽으로 x칸만큼 회전
    for _ in range(len(s)):
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
                continue    # 첫 번째 if문 실행 시, 두 번째 if문 실행이 불필요하므로 바로 다음으로 넘어감
    
            # 괄호가 순서로 한 쌍일 경우 stack 리스트에서 제거 
            if stack[-1] == "(" and i == ")":
                stack.pop()
            elif stack[-1] == "[" and i == "]":
                stack.pop()
            elif stack[-1] == "{" and i == "}":
                stack.pop()
            else:
                stack.append(i)
    
        # 괄호가 모두 쌍일 경우 answer에 + 1
        if not stack:
            answer += 1
        
        # 왼쪽으로 한 칸 이동
        s = s[1:] + s[0]

    # 출력
    return answer