# 10 진수에서 q진법으로 변환하는 함수 정의
def conversion(n, q):
    # 변수 정의 
    result = ""
    
    # 나머지를 순서대로 구한 후 역순 출력
    while n > 0:
        n, mod = divmod(n, q)
        result += str(mod)
    
    return result[::-1]

def solution(n):
    return int(conversion(n, 3)[::-1], 3)