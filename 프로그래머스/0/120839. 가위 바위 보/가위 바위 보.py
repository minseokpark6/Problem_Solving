def solution(rsp):
    rsp = list(rsp)
    answer = []
    for i in rsp:
        if i == '2':
            answer.append('0')
        elif i == '0':
            answer.append('5')
        else:
            answer.append('2')
    answer = ''.join(answer)
    return answer