def solution(n, a, b):
    # 변수 지정
    round = 0 
    
    # 몇 라운드에서 만나는지 확인 
    while a != b:
        a = (a+1) // 2
        b = (b+1) // 2
        round += 1
    
    # 출력
    return round
    


'''
(1) 반복문 좀 더 직관적으로 변경 -> 굳이 for문으로 제한할 필요가 없음 
(2) if else 문 보다 +1 후 몫을 구하면 더 간단한 코드 구현 가능


## 2차 통과 코드 

import math
def solution(n, a, b):
    # 몇 라운드에서 만나는지 카운트
    for i in range(int(math.log2(n))):
        a = a//2 if a%2==0 else (a//2)+1
        b = b//2 if b%2==0 else (b//2)+1
        
        # 만났는지 확인 후 출력
        if a == b:
            return i+1


## 기존 통과 코드 
def solution(n,a,b):
    answer = 0
    
    # 몇 라운드에서 만나는지 카운트
    while True:
        # 1라운드씩 증가
        answer += 1
        
        # 모두 짝수로 맞춰주기
        if a%2 == 1:
            a+=1
        if b%2 == 1:
            b+=1
            
        # a와 b가 맞붙는 라운드인지 확인
        if a//2 == b//2:
            break
        else:
            a, b = a//2, b//2
    # 출력
    return answer
'''