def solution(myStr):
    li = myStr.replace("a", " ").replace("b", " ").replace("c", " ").split(" ")
    answer = [s for s in li if s != ""]
    if len(answer) == 0:
        answer = ["EMPTY"]
    return answer