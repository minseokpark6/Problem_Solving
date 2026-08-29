def solution(order):
    return sum(5000 if "latte" in o else 4500 for o in order)

'''
def solution(order):
    answer = 0
    for o in order:
        if "americano" in o:
            answer += 4500
        elif "latte" in o:
            answer += 5000
        elif o == "anything":
            answer += 4500
    return answer
'''