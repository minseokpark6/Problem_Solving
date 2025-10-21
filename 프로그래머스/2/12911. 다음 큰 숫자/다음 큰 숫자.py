def solution(n):
    # n을 이진수로 변환 후 1의 개수 카운트 
    cnt = bin(n).count('1')

    # 다음 큰 숫자 찾기 
    while True:
        n += 1
        if bin(n).count('1') == cnt:
            return n
        
"""

## 기존 통과 코드
def solution(n):
    # 자연수 n을 2진수로 변환 후 1의 개수 카운트
    b1 = format(n, 'b')
    b1_count = b1.count("1")
    
    # 다음 큰 숫자 찾기 
    while True:
        n += 1
        b2 = format(n, 'b')
        b2_count = b2.count("1")
        if b1_count == b2_count:
            answer = n
            break
    # 출력
    return answer



1. 
파이썬 내장함수 bin(), oct(), hex() >> 2진수, 8진수, 16진수로 변환 

value = 60

b = bin(value)
o = oct(value)
h = hex(value)

print(b)
print(o)
print(h)
------------------------------------------
# 0b111100
# 0o74
# 0x3c


1-1. format함수 사용 시 숫자만 출력 가능 

value = 60

b = format(value, 'b')
o = format(value, 'o')
h = format(value, 'x')

print(b)
print(o)
print(h)
------------------------------------------
# 111100
# 74
# 3c


2. 다른 진수 형태에서 10진수로 변환 

b = int(b, 2)
o = int(o, 8)
h = int(h, 16)

"""
