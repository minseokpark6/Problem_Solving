def solution(n):
    # 변수 설정
    answer = 0
    # 연속한 자연수들로 n을 구하는 개수 구하기 
    for i in range(1, n+1):
        sum = 0
        num = i
        while sum < n:
            sum += num
            num += 1
        if sum == n:
            answer += 1
    # 출력
    return answer