def is_parallel(a, b, c, d):
    # 기울기 구하기
    g1 = (a[1] - b[1]) / (a[0] - b[0])
    g2 = (c[1] - d[1]) / (c[0] - d[0])
    
    # 출력
    return 1 if g1 == g2 else 0 

def solution(dots):
    # 3가지 경우의 수의 평행 여부 확인
    p1 = is_parallel(dots[0], dots[1], dots[2], dots[3])
    p2 = is_parallel(dots[0], dots[2], dots[1], dots[3])
    p3 = is_parallel(dots[0], dots[3], dots[1], dots[2])
    
    # 출력
    return 1 if 1 in [p1, p2, p3] else 0

"""
(1) 기울기가 같으면 평행 
    - 기울기: y축의 변화량 / x축의 변화량
    
(2) 네 개의 점을 두 개씩 연결하는 경우의 수 => 총 3가지
"""