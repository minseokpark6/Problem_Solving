def solution(s):
    temp = []
    for i in s:
        if s.count(i) == 1:
            temp.append(i)
    answer = ''.join(sorted(temp))
    return answer