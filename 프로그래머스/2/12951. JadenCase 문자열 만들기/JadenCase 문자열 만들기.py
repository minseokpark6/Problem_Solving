def solution(s):
    return " ".join(w.capitalize() if w else w for w in s.split(" "))


'''
(1) capitalize 메소드 활용 
- 단어의 첫 글자는 대문자로 나머지는 소문자로 변환해주는 파이썬 메소드 

(2) 제너레이터 표현식 
- 불필요한 리스트 사용을 없애서 메모리 절약

### 이전 통과 코드

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
        if w:
            z = w[0].upper() + w[1:]
        else:
            z = w
        result.append(z)
    
    ## 파이썬에서 if i:는 i가 빈 문자열이 아닌 경우 참(True)으로 작동하고, i가 빈 문자열('')이면 거짓(False)으로 작동합
    
    """
    
    # 출력
    return " ".join(result)
'''

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