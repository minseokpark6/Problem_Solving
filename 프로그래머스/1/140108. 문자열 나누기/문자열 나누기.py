from collections import deque

def solution(s):
    # 변수 정의
    dq = deque(s)
    cnt = 0
    x_cnt, other_cnt = 0, 0
    first = None

    # 문자열 분해
    while dq:

        # 비교할 문자 정의
        char = dq.popleft()
        
        # x가 없는 경우
        if first is None:
            first = char
            x_cnt += 1
            continue

        # x와 x가 아닌 문자 비교
        if first == char:
            x_cnt += 1
        
        else:
            other_cnt += 1
        
        # x와 x가 아닌 문자의 횟수 비교
        if x_cnt == other_cnt:
            cnt += 1
            first = None
            x_cnt, other_cnt = 0, 0

    # 출력
    return cnt + (1 if first else 0)

'''
이전 코드 대비 개선점 
1) 불필요한 리스트 사용 >> 숫자 카운트로 대체 
2) deque를 사용하여 pop()의 시간 복잡도를 O(n)에서 O(1)로 감소
'''


'''>> 이전 코드 
def solution(s):
    # 변수 설정
    answer = 0
    first, other = [], []
    s = list(s)
    
    # 분해한 문자열 개수 카운트
    while len(s) > 0:
        if not first:
            first.append(s[0])
            s.pop(0)
            continue
        
        if first[-1] == s[0]:
            first.append(s[0])
            s.pop(0)

        elif first[-1] != s[0]:
            other.append(s[0])
            s.pop(0)
            
            if len(first) == len(other):
                answer += 1
                first, other = [], []

    # 출력
    return answer if not first else answer + 1
'''
    