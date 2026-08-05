def solution(binomial):
    # 변수 정의
    arr = binomial.split(" ")
    a, op, b = int(arr[0]), arr[1], int(arr[2])
    
    # 출력
    if op == "+":
        return a+b
    elif op == '-':
        return a-b
    else:
        return a*b
    
'''
def solution(binomial):
    result = binomial.split(" ")
    a, b = int(result[0]), int(result[2])
    if result[1] == "+":
        answer = a + b
    elif result[1] == "-":
        answer = a - b
    else:
        answer = a*b
    return answer
'''