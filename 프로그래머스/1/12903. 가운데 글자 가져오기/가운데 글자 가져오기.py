def solution(s):
    # 가운데 글자 인덱스 지정
    idx = len(s)//2
    # 출력
    return s[idx] if len(s)%2 != 0 else s[idx-1:idx+1]

''' >> 이전 코드 

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
'''