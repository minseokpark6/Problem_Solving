def solution(myString):
    result = myString.split("x")
    answer = [len(str) for str in result]
    return answer