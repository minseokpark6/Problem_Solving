def solution(balls, share):
    # 변수 정의
    result = 1

    # balls의 개수에서 share개를 뽑는 경우의 수 조합
    for i in range(1, share+1):
        result = result * (balls - i + 1) // i

    # 출력
    return result
   

'''
def solution(balls, share):
    a = 1
    b = 1
    for i in range(share + 1, balls + 1):
        a *= i
    for j in range(1, (balls-share+1)):
        b *= j

    answer = a / b
    
    return answer
'''