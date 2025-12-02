from collections import Counter

def solution(want, number, discount):
    # 변수 지정
    cnt = 0
    dic = {w:n for w, n in zip(want, number)}
    
    # 구매하고자 하는 제품과 세일 제품 비교
    for i in range(len(discount)):
        if dic == Counter(discount[i:i+10]):
            cnt += 1
    
    # 출력
    return cnt



'''


## 기존 통과 코드 

from collections import Counter

def solution(want, number, discount):
    # 변수 지정
    cnt = 0
    dic = {w:n for w, n in zip(want, number)}
    
    # 구매하고자 하는 제품과 세일 제품 비교
    for i in range(len(discount)):
        if dic == Counter(discount[i:i+10]):
            cnt += 1
    
    # 출력
    return cnt

## Counter 메소드를 사용하지 않은 코드 

def solution(want, number, discount):
    # 변수 지정 
    cnt = 0
    want_dic = {w:n for w, n in zip(want, number)}
    
    # 모두 할인 받을 수 있는 회원 등록 날짜의 총 일수 카운트 
    for i in range(len(discount)):
        
        # 10일 간 할인 품목 정리
        dic = {}
        for product in discount[i:i+10]:
            if product in dic:
                dic[product] += 1
            else:
                dic[product] = 1

        # 구매리스트와 비교 
        if want_dic == dic:
            cnt += 1
    
    # 출력 
    return cnt
'''