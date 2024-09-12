def solution(x):
    # 각 자리 수의 합 구하기
    x_list = [int(i) for i in str(x)]
    s = sum(x_list)
    # 하샤드 수 검사
    if x % s == 0:
        return True
    else:
        return False