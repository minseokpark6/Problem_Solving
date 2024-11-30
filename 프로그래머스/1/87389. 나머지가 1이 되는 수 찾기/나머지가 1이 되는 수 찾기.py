def solution(n):
    # 변수 설정
    num = 2
    # 나머지가 1이 되는 가장 작은 수 찾기
    while True:
        if n%num == 1:
            answer = num
            break
        num +=1

    # 출력
    return answer