def solution(myString, pat):
    result = "".join(["B" if s == "A" else "A" for s in myString])
    if pat in result:
        answer = 1
    else:
        answer = 0
    return answer