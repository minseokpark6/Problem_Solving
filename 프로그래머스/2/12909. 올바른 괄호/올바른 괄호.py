def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:  # i == ")"
            if not stack:  # 스택이 비어 있는데 닫는 괄호가 나오면 실패
                return False
            stack.pop()
    return not stack  # 비어있으면 True, 남아있으면 False

'''
# 불필요한 부분 삭제 
- if not stack >> else에 포함 가능 
- 출력 시 코드 간소화 


# 기존 성공 코드 
def solution(s):
    stack = []
    for i in s:
        # 스택 리스트가 비어있는 경우, 추가
        if not stack:
            stack.append(i)
            continue    # 첫 번째 if문 실행 시, 두 번째 if문 실행이 불필요하므로 바로 다음으로 넘어감
    
        # 괄호가 "(" ")" 순서로 한 쌍일 경우 stack 리스트에서 제거 
        if stack[-1] == "(" and i == ")":
            stack.pop()
        else:
            stack.append(i)
    
    # 출력 
    # >> stack이 빈리스트가 아닐 경우 괄호가 짝지어져 나온 것이 아님으로 False 출력
    # >> 비어있을 경우 괄호가 짝지어져 있을 경우 스택 리스트가 빈 리스트로 나옴 
    return False if stack else True
            
        
    
    
## 오답 

>> 반례: "(()))("

def solution(s):

    # 변수 설정
    a,b = 0, 0

    # 괄호의 개수 구하기
    for i in s:
        if i == "(":
            a += 1
        elif i == ")":
            b += 1

    # 괄호가 먼저 열리고, 개수가 같은 경우만 True
    if (a == b) and (s[0] == "("):
        answer = True
    else:
        answer = False

    # 출력
    return answer
'''