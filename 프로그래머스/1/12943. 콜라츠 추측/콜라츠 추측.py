def solution(n):
    # 변수 정의 
    cnt = 0
    
    # 콜라츠 추측 횟수 구하기
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (n*3)+1
        cnt += 1
    
        # 500번이 되었는데 1이 되지 않은 경우
        if cnt == 500 and n != 1:
            return -1
            break
        
    return cnt

''' 이전 코드
def solution(num):
    answer = 0
    
    # 주어진 숫자가 1인 경우
    if num == 1:
        return 0
    
    while answer < 500:
        # 횟수 추가 
        answer += 1
    
        # num이 각각 짝수/홀수 일때 연산
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1
        
        if num == 1:
            return answer
            break
            
        # 500번 작업할 때 까지 1이 되지 않았다면 Stop
        elif (answer == 500) and (num != 1):
            return -1
            break
    
'''