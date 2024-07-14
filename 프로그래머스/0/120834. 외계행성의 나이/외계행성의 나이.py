def solution(age):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    answer = []
    for i in list(str(age)):
        answer.append(alpha[int(i)])
    answer = ''.join(answer)
    return answer
