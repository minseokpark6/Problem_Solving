# 11~15 숫자 아스키코드로 변환하는 함수 설정
def digit_to_char(n):
    return str(n) if n < 10 else chr(ord('A') + (n - 10))

# n진법으로 변환하는 함수 설정 
def convert_to_n(n, q):
    if n==0 :
        return '0'
    
    result = ''
    
    while n > 0:
        n, mod = divmod(n, q)
        result = digit_to_char(mod) + result
        
    return result

# 말해야 하는 숫자 구하는 함수 정의
def solution(n, t, m, p):
    number = ''
    num = 0
    # n진법으로 변환한 문자열 구하기 
    while len(number) < t * m:
        number += convert_to_n(num, n)
        num += 1
     # 말해야하는 숫자 t개 출력
    return ''.join([number[i] for i in range(p - 1, t * m, m)])