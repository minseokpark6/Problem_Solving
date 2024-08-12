def solution(myString):
    answer = []
    result = myString.split("x")
    answer = [s for s in result if s != ""]
    return sorted(answer)