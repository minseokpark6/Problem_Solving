def solution(a, b):
    # 변수정의
    r1 = int(str(a) + str(b))
    r2 = 2*a*b
    return r1 if r1 >= r2 else r2
