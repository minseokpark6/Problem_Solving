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