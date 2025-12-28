# 정렬 ver 코드
def solution(phone_book):
    # 정렬 -> 같은 접두어를 가진 번호가 바로 다음에 오도록 
    arr = sorted(phone_book)
    
    # 접두어 여부 확인 
    for idx in range(len(arr)-1):
        if arr[idx+1].startswith(arr[idx]):
            return False
    
    # 출력
    return True

'''
## 해시 ver 코드
def solution(phone_book):
    # 해시 자료 구조로 변경 
    numbers = set(phone_book)
    
    # 접두어 검색
    for number in numbers:
        prefix = ''
        for c in number:
            prefix += c
            if prefix in numbers and prefix != number:
                return False
    # 출력
    return True
    

## 기존 통과 코드 
def solution(phone_book):
    # 변수 정의
    answer = True
    
    # 사전 순서대로 정렬 >> 만약 같은 접두어를 가진 번호라면 바로 다음에 오게 되어 있음
    phone_book.sort()
    
    # 접두어가 있는지 확인
    for idx in range(len(phone_book) - 1):
        if phone_book[idx] == phone_book[idx+1][:len(phone_book[idx])]:
            answer = False
            break
    # 출력
    return answer
'''