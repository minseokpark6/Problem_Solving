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


"""


def solution(n,a,b):
    answer = 0
    
    # 몇 라운드에서 만나는지 카운트
    while True:
        # 1라운드씩 증가
        answer += 1
        
        # 모두 짝수로 맞춰주기
        if a%2 != 0:
            a+=1
        elif b%2 != 0:
            b+=1
            
        # a와 b가 맞붙는 라운드인지 확인
        if a//2 == b//2:
            break
        else:
            a, b = a//2, b//2
    # 출력
    return answer


"""