def solution(s, skip, index):
    
    # 영문 소문자 리스트 생성 
    alph = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    length = len(alph)
    
    # 소문자 인덱스 -> 딕셔너리로 매핑
    char_to_idx = {char:i for i, char in enumerate(alph)}

    # 문자 변환 
    answer = []
    for ch in s:
        idx = (char_to_idx[ch]+index)%length
        answer.append(alph[idx])

    # 출력
    return "".join(answer)


'''
## 수정 사항 
1) list.index() >> 매 번 index를 찾기 위해 리스트의 길이만큼 돌아야 함 
>> 딕셔너리로 해결 

2) circle 사용 
>> alph의 길이와 나머지를 이용하여 불필요한 연산 및 실수 제거


'''


''' >> 기존 코드 

def solution(s, skip, index):
    answer = ''
    # 영문 소문자 리스트 생성 // skip에 들어가있는 문자 제외
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
'''


"""
1. chr() 함수 
- 유니코드 값을 문자로 변환하는 함수
- 97-122까지가 소문자 알파벳 a-z까지 해당 
"""