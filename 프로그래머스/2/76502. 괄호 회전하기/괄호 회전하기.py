# 문자열이 올바른 괄호 문자열인지 확인하는 함수 정의 
def is_valid(s):
    # 변수 정의 
    stack = []
    pairs = {']':'[', '}':'{', ')':'('} # 닫는 괄호를 기준으로 열린 괄호가 스택에 있나 비교를 위한 딕셔너리 
    opens = set('({[')  # in을 통한 빠른 비교를 위해 set으로 정의 
    
    # 올바른 괄호 문자열인지 확인 
    for ch in s:
        if ch in opens:
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return not stack

# 회전 시키면서 카운트하는 함수 정의
def solution(s):
    # 변수 정의
    n = len(s)
    cnt = 0
    
    # 문자열 회전을 슬라이싱 없이 처리하기 위해 
    doubled = s + s
    
    # 문자열 회전
    for start in range(n):
        # 'start - start + n' 까지를 회전된 문자열로 간주
        if is_valid(doubled[start:start+n]):
            cnt += 1
    
    # 출력
    return cnt


'''
## 개선 사항
(1) 올바른 괄호를 확인하는 함수 + 문자열 회전 함수 분리 작성 >> 코드 가독성 개선 
(2) 괄호 매칭을 if - elif - else 문 대신 딕셔너리로 변경 >> 코드 가독성 개선
(3) s = s[1:] + s[0] >> 회전 성능 개선


## 이전 통과 코드 

def solution(s):
    # 변수 정의 
    cnt = 0

    # 올바른 괄호 문자열 카운트 
    for _ in range(len(s)):
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
                continue
            
            # 괄호가 순서대로 한 쌍일 경우 
            if stack[-1] == "(" and i== ")":
                stack.pop()
            elif stack[-1] == "[" and i== "]":
                stack.pop()
            elif stack[-1] == "{" and i== "}":
                stack.pop()
            else:
                stack.append(i)
            
        # 괄호가 모두 쌍일 경우 
        if not stack:
            cnt += 1
        
        # 왼 쪽으로 한 칸 이동
        s = s[1:] + s[0]

    # 출력
    return cnt
    '''