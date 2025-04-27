import sys
input = sys.stdin.readline
# 문자 입력
while True:
    s = input().rstrip()
    # 정지 조건 
    if s == '.':
        break
    # 스택 생성 및 균형 여부
    stack = []
    is_balanced = True
    # 문자열 확인
    for w in s:
        # 왼쪽 괄호일 경우 스택에 추가
        if w in '[(':
            stack.append(w)
        # 오른쪽 소괄호일 경우
        elif w == ')':
            # 스택이 비어있거나, 괄호의 쌍이 맞지 않을 경우
            if not stack or stack[-1] != '(':
                is_balanced = False
                break
            # 스택에 원소가 들어가있고, 괄호의 쌍이 맞을 경우
            stack.pop()
        # 오른쪽 대괄호의 경우
        elif w == ']':
            # 스택이 비어있거나, 괄호의 쌍이 맞지 않을 경우
            if not stack or stack[-1] != '[':
                is_balanced = False
                break
            # 스택에 원소가 들어가있고, 괄호의 쌍이 맞을 경우
            stack.pop()
    # 출력
    print("yes" if not stack and is_balanced else 'no')
        
            