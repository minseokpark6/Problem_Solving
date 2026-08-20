def solution(intStrs, k, s, l):
    return [int(i[s:s+l]) for i in intStrs if int(i[s:s+l]) > k]

'''
def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        ret = intStr[s:s+l]
        if int(ret) > k :
            answer.append(int(ret))
    return answer
'''