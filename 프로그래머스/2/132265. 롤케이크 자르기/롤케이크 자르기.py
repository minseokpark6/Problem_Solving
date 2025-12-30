from collections import Counter 

def solution(topping):
    # 변수 정의 
    cnt = 0
    
    # 우선 한 쪽이 모두 먹는다고 가정 
    older_bro = dict(Counter(topping))
    younger_bro = set()
    
    # 토핑의 개수가 일치하는 경우 카운트 
    for t in topping:
        # 철수의 롤케이크에서 토핑 제거 
        older_bro[t] -= 1
        if older_bro[t] == 0:
            del older_bro[t]
        
        # 동생의 롤케이크에 토핑 추가 
        younger_bro.add(t)
        
        # 토핑의 개수가 같은 경우 카운트 
        if len(older_bro) == len(younger_bro):
            cnt += 1

    # 출력        
    return cnt