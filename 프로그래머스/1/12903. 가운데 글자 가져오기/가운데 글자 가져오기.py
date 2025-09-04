def solution(s):
    idx = len(s)//2
    # 홀수인 경우
    if len(s) % 2 != 0:
        answer = s[idx]
    # 짝수인 경우
    else:
        answer = s[idx-1:idx+1]
    
    # 출력 
    return answer