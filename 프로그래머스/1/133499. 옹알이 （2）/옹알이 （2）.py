def solution(babbling):
    # 변수 설정
    words = ["aya", "ye", "woo", "ma"]
    cant = ["ayaaya", "yeye", "woowoo", "mama"]

    # 발음 가능한 단어 변경
    for i in range(len(babbling)):
        # 연속으로 오는 word는 변경 불가능
        for c in cant:
            babbling[i] = babbling[i].replace(c, "x")

        # 발음 가능한 단어는 " "로 치환
        for word in words:
            babbling[i] = babbling[i].replace(word, " ")

        # 카운팅을 위해 " "를 ""로 치환
        babbling[i] = babbling[i].replace(" ", "")
    
    # 출력
    return babbling.count("")


