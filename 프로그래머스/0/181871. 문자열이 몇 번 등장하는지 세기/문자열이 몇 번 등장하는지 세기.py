def solution(myString, pat):
    return sum(
    myString[i:i+len(pat)] == pat for i in range(len(myString) - len(pat) +1)
    )

'''
def solution(myString, pat):
    answer = 0
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            answer += 1
    return answer
'''