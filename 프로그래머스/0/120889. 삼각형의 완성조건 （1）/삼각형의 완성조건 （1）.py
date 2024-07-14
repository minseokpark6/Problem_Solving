def solution(sides):
    l1 = max(sides)
    sides.remove(l1)
    sum = 0
    for side in sides:
        sum += side
    if l1 < sum :
        return 1
    else:
        return 2