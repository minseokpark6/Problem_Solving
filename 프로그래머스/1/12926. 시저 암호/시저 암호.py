
def solution(s, n):
    # 변수 정의 
    result = []
    
    # 시저 암호화 
    for c in s:
        if c.isalpha():
            result.append(
                chr((ord(c) - ord('a')+n) % 26 + ord('a')) if c.islower() else chr((ord(c) - ord('A')+n) % 26 + ord('A'))
            )
        else:
            result.append(c)

    # 출력 
    return "".join(result)

''' 
(1) list.index() => 매우 비효율적
- 아스키 코드의 ord()를 활용하여 직접 계산 수행

(2) 불필요한 문자열 리스트 사용 
- 나머지 연산으로 불필요한 순환 피할 수 있음

(3) 문자열 누적합 - 메모리로 인한 성능저하 
- 리스트로 대체 후 "".join() 사용

### 기존 통과 코드 

def solution(s, n):
    # 변수 정의 
    result = ''
    ch = [chr(i) for i in range(97, 123)] * 2
    # 시저 암호화
    for c in s:
        if c == " ":
            result += c
        else:
            result += ch[ch.index(c)+n] if c.islower() else ch[ch.index(c.lower())+n].upper()
    # 출력
    return result
'''