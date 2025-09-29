def solution(s):
    return (len(s) in (4, 6)) and s.isdigit()

'''
(1) 파이썬 내장 메소드 활용 
- isdigit() => 문자열이 숫자인지 판별하는 메소드 

(2) len(s) in (4, 6) >> 코드 간결화 

(3) True or False를 묻는 질문이기 때문에 굳이 복잡하게 변수를 저장할 필요 없음 


### 이전 코드 
def solution(s):
    answer = False
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i in num:
                answer = True
            else:
                answer = False
                break
    return answer

'''