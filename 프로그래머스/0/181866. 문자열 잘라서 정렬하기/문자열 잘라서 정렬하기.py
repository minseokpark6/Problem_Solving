def solution(myString):
    return sorted(s for s in myString.split("x") if s != "")

'''
def solution(myString):
    answer = []
    result = myString.split("x")
    answer = [s for s in result if s != ""]
    return sorted(answer)
'''