def solution(n):
    # n의 제곱근 구하기
    sqrt = n ** (0.5)
    # 제곱근이 정수일 경우 
    if sqrt % 1 == 0:
        return (sqrt+1) ** 2
    # 제곱근이 정수가 아닐 경우 
    else:
        return -1