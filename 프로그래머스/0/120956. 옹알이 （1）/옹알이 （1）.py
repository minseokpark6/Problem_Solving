def solution(babbling):
    # 변수 지정
    words = ['aya', 'ye', 'woo', 'ma']

    # 발음 가능한 단어를 " "으로 치환 
    for i in range(len(babbling)):
        for word in words:
            babbling[i] = babbling[i].replace(word, " ")
        # " "을 ""로 치환
        babbling[i] = babbling[i].replace(" ", "")
    
    # 발음 가능한 단어("") 카운트
    return babbling.count("")


"""
(1) 조카가 발음 가능한 문자열을 공백(" ")으로 치환
(2) 공백(" ")을 ""로 치환 
    - 중복된 단어 사용의 경우 공백이 겹쳐서 나옴으로 카운팅하기가 어려움 
(3) ""를 count
"""