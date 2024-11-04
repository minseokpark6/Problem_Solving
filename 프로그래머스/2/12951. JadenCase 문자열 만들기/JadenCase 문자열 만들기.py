def solution(s):
    # 모든 문자 소문자화
    s = s.lower()
    # 공백을 기준으로 분리
    word = s.split(" ")

    # 단어 맨 앞 글자 대문자화하는 리스트 컴프리헨션
    result = [w[0].upper() + w[1:] if w else w for w in word]
    
    """
    # for문 
    result = []
    
    for w in word: 
        if i:
            z = w[0].upper() + w[1:]
        else:
            z = i
        result.append(z)
    
    ## 파이썬에서 if i:는 i가 빈 문자열이 아닌 경우 참(True)으로 작동하고, i가 빈 문자열('')이면 거짓(False)으로 작동합
    
    """
    
    # 출력
    return " ".join(result)


"""
>> 반례 : 스페이스가 두 개이상 나온 경우

def solution(s):
    # 모든 문자 소문자화
    s = s.lower()
    # 공백을 기준으로 분리
    word = s.split(" ")

    # 단어 맨 앞 글자 대문자화
    result = [w[0].upper() + w[1:] for w in word]
    
    # 출력
    return " ".join(result)
"""