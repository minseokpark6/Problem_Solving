def solution(s):
    return " ".join(
       "".join(ch.upper() if idx%2==0 else ch.lower() for idx, ch in enumerate(word)) 
       for word in s.split(" ")
    )

'''
(1) 문자열 +=  => append + join으로 변경 
- 파이썬의 문자열은 **불변 객체(immutable)**라서, temp += w.upper()처럼 문자열을 반복해서 붙이면 매번 새로운 문자열 객체가 만들어져 메모리 낭비 발생
- append + join이 효율적 
- 시간 복잡도 역시 O(n²) -> O(n)

## 이중 리스트 컴프리헨션으로 간소화 시키기 전 코드 

def solution(s):
    # 리스트 생성 
    result = []
    
    # 이상한 문자 만들기 
    for word in s.split(" "):
        temp = [
            w.upper() if idx%2==0 else w.lower()
            for idx, w in enumerate(word)
        ]
        result.append("".join(temp))

    # 출력 
    return " ".join(result)


## 기존 통과 코드

def solution(s):
    # 변수 지정
    words = s.split(" ")
    result = []

    # 이상한 문자 만들기
    for word in words:
        temp = ""
        for idx, w in enumerate(word):
            if idx%2==0:
                temp+= w.upper()
            else:
                temp+= w.lower()
        result.append(temp)

    # 출력 =
    return " ".join(result)
'''