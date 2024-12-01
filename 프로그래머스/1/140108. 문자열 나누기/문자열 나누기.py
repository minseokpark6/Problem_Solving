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