from collections import Counter

def solution(want, number, discount):
    # 변수 지정
    answer = 0
    dic = {w:n for w, n in zip(want, number)}
    
    # 구매하고자 하는 제품과 세일 제품 비교
    for i in range(len(discount)):
        if dic == Counter(discount[i:i+10]):
            answer += 1
    
    # 출력
    return answer

