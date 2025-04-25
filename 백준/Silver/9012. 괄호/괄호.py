import sys
input = sys.stdin.readline
# 테스트 데이터 개수 
t = int(input())
# VPS 여부 출력
for _ in range(t):
    s = input().strip()
    stack = []
    is_valid = True

    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                is_valid = False
                break
    
    # 스택이 비어 있어야 VPS임
    print("YES" if is_valid and not stack else "NO")