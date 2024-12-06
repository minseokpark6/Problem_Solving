def solution(n, m, section):
    # 무조건 한 번은 페인트를 칠해야하니까 기본 값을 1로 두고
    answer = 1
    # 페인트칠의 기준이 될 변수 설정
    standard = section[0]

    # 페인트 칠을 해야하는 section이 기준에서 롤러의 길이 내에 포함되는지 확인
    for s in section:
        if standard + (m-1) < s:
            standard = s 
            answer += 1
    # 출력
    return answer