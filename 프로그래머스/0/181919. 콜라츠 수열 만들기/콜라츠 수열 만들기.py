def solution(n):
    # 변수 정의
    result = [n]
    
    # 콜라츠 수열 생성
    while n != 1:
        n = n//2 if n%2==0 else (n*3)+1
        result.append(n)
    
    # 출력
    return result

'''
def solution(n):
    answer = []
    answer.append(n)
    while True:
        # 짝수일 경우
        if n % 2 == 0:
            n = n // 2
        # 홀수일 경우    
        else :
            n = (3 * n) + 1
        # 리스트에 연산값 추가
        answer.append(n)
        # 정지 조건 설정
        if n == 1:
            break
    
    return answer
'''