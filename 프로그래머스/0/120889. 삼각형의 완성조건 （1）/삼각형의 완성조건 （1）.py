def solution(sides):
    # 변의 길이 오름차순 정렬
    arr = sorted(sides, reverse=True)
    return 1 if arr[0] < arr[1]+arr[2] else 2


'''
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
'''