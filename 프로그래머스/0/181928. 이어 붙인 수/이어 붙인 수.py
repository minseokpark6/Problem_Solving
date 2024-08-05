def solution(num_list):
    # 빈 문자열 생성
    o = ''
    e = ''
    # 홀수, 짝수 구분해서 이어 붙이기
    for num in num_list:
        if num % 2 == 1:
            o += str(num)
        else:
            e += str(num)
    # 두 수의 합 구하기
    answer = int(o) + int(e)
    
    return answer