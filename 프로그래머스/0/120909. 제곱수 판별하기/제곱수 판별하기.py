def solution(n):
    li = []
    for i in range(1, 1001):
        squared = i ** 2
        li.append(squared)
    if n in li :
        return 1
    else:
        return 2