def solution(n):
    # 빈 리스트 생성 
    result = []
    # 3진법의 역순 구하기 
    while n>0:
        n, mod = divmod(n, 3)
        result.append(str(mod))
    # 10진법으로 출력 
    return int("".join(result), 3)


'''
(1) 불필요한 [::-1] 중복 없애기 
(2) 파이썬에서 문자열 +=은 매번 새로운 문자열 객체를 생성 
- 비효울적
- append + join이 훨씬 효율적

## 이전 통과 코드
def conversion(n, q):
    # 변수 정의 
    result = ""
    # 나머지를 순서대로 구한 후 
    while n>0:
        n, mod = divmod(n, q)
        result += str(mod)
    # 역순으로 출력
    return result

def solution(n):
    return int(conversion(n, 3)[::-1], 3)
    
'''