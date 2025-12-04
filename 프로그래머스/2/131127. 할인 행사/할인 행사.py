from collections import Counter

def solution(want, number, discount):
    # 변수 지정
    cnt = 0
    need = {w:n for w, n in zip(want, number)}
    window = Counter(discount[:10])     # 첫 윈도우 정의
    
    # 첫 윈도우 비교 
    if need == window:
        cnt += 1
    
    # 이후 윈도우와 구매하고자 하는 제품 비교
    for i in range(10, len(discount)):
        # 한 칸씩 슬라이싱 
        out_product = discount[i-10]
        in_product = discount[i]
        
        # 빠지는 제품 카운트 감소
        window[out_product] -= 1
        if window[out_product] == 0:
            del window[out_product]
        
        # 새로 추가된 제품 카운트 
        window[in_product] += 1
        
        # 비교
        if window == need:
            cnt += 1  
    
    # 출력
    return cnt



'''
## 개선점 
(1) for문 내 'Counter(discount[i:i+10])' >> 매번 슬라이싱이 들어가는 것이 비효율적 
- 슬라이싱 윈도우로 해결 가능


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