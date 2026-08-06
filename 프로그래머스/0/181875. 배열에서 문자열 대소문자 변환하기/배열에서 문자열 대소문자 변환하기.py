def solution(strArr):
    return [s.upper() if idx%2!=0 else s.lower() for idx, s in enumerate(strArr)]

'''
def solution(strArr):
    answer = []
    for idx, s in enumerate(strArr):
        if idx % 2 == 0:
            s = s.lower()
        else:
            s = s.upper()
        answer.append(s)
    return answer
'''