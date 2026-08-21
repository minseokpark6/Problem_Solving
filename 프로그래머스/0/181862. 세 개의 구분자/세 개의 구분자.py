def solution(myStr):
    # 구분자 변환
    for sep in "abc":
        myStr = myStr.replace(sep, " ")
    
    # 출력
    return myStr.split() or ["EMPTY"]

'''
def solution(myStr):
    li = myStr.replace("a", " ").replace("b", " ").replace("c", " ").split(" ")
    answer = [s for s in li if s != ""]
    if len(answer) == 0:
        answer = ["EMPTY"]
    return answer
'''