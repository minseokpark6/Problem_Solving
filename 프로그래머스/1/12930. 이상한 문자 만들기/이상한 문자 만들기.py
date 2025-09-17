def solution(s):
    # 변수 지정
    result = []
    words = s.split(" ")
    
    # 문자열 변경
    for word in words:
        temp = ""
        for idx, w in enumerate(word):
            if idx % 2 == 0:
                temp += w.upper()
            else:
                temp += w.lower()
        result.append(temp)
    
    # 출력
    return " ".join(result)