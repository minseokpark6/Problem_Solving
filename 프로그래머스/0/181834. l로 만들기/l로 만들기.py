def solution(myString):
    return "".join("l" if char < "l" else char for char in myString)


'''
def solution(myString):
    alpha = ["a", "b", "c", "d", "e", "f", 'g', "h", "i", "j", "k"]
    answer = []
    for s in myString:
        if s in alpha:
            answer.append("l")
        else:
            answer.append(s)
    answer = "".join(answer)
    return answer
'''