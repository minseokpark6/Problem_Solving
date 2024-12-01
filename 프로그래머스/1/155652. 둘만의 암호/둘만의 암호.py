def solution(s, skip, index):
    answer = ''
    # 영문 소문자 리스트 생성 
    alph = [chr(i) for i in range(97, 123)]
    # skip에 들어가 있는 문자 제거 
    for sk in skip:
        if sk in alph:
            alph.remove(sk)
    # circle
    alph *= 5
    
    # 문자 대체
    for a in s:
        idx = alph.index(a) + index
        answer += alph[idx]

    # 출력
    return answer


"""
1. chr() 함수 
- 유니코드 값을 문자로 변환하는 함수
- 97-122까지가 소문자 알파벳 a-z까지 해당 
"""