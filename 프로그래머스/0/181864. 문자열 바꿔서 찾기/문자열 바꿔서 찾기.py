def solution(myString, pat):
    # 변수 정의
    result = "".join("B" if s == "A" else "A" for s in myString)
    # 출력
    return 1 if pat in result else 0

'''
def solution(myString, pat):
    result = "".join(["B" if s == "A" else "A" for s in myString])
    if pat in result:
        answer = 1
    else:
        answer = 0
    return answer
'''