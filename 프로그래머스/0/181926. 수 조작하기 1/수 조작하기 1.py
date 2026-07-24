def solution(n, control):
    # 동작 값 정의 
    move = {
        "w" : 1,
        "s" : -1,
        "d" : 10,
        "a" : -10
    }

    # control 순서에 따라 변경
    for c in control:
        n += move[c]
    
    # 출력
    return n

'''
def solution(n, control):
    for s in control:
        if s == 'w':
            n += 1
        elif s == 's':
            n -= 1
        elif s == 'd':
            n += 10
        elif s == 'a':
            n -= 10

    return n
'''