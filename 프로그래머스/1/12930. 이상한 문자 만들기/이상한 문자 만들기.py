def solution(s):
    result = []
    words = s.split(" ")
    
    for word in words:
        w = ""
        for idx, s in enumerate(word):
            if idx % 2 == 0:
                w += s.upper()
            else:
                w += s.lower()
        result.append(w)
        
    answer = " ".join(result)
    return answer