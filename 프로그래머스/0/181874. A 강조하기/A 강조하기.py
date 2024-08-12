def solution(myString):
    result = myString.lower()
    answer = ""
    for s in result:
        if s == "a":
            answer += s.upper()
        else:
            answer += s
    return answer