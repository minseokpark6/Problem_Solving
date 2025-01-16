from collections import Counter
def solution(topping):
    # 변수 정의
    answer = 0
    
    # 철수와 동생이 케익을 나누는 변수 정의
    cheol = dict(Counter(topping))   # 우선 철수가 케익을 모두 먹는다고 가정
    bro = set()
    
    # 토핑의 개수가 일치하는 경우 카운트 
    for top in topping:
        # 철수가 먹은 토핑에서 1개 개수 제거
        cheol[top] -= 1
        
        # 개수가 0인 경우 cheol에서 삭제
        if cheol[top] == 0:
            del cheol[top]
        
        # bro에 토핑 추가
        bro.add(top)
        
        # 길이가 같은 경우 카운트
        if len(bro) == len(cheol):
            answer += 1

    # 출력
    return answer