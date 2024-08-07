def solution(numLog):
    temp = []
    for i in range(len(numLog) - 1):
        a = numLog[i+1] - numLog[i]
        if a == 1:
            temp.append('w')
        elif a == -1:
            temp.append('s')
        elif a == 10:
            temp.append('d')
        elif a == -10:
            temp.append('a')
    answer = "".join(temp)         
    return answer