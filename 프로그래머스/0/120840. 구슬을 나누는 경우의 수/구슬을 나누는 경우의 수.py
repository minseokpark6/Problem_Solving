def solution(balls, share):
    a = 1
    b = 1
    for i in range(share + 1, balls + 1):
        a *= i
    for j in range(1, (balls-share+1)):
        b *= j

    answer = a / b
    
    return answer