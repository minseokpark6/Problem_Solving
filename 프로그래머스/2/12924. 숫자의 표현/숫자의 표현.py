def solution(n):
    # 변수 정의 
    cnt = 0
    left, right, total = 1, 1, 1
    
    # 연속하는 자연수로 n이 표현되는 경우의 수
    while left <= n:
        if total < n:
            right += 1
            total += right
    
        elif total > n:
            total -= left
            left += 1

        else:
            cnt += 1
            total -= left 
            left += 1
    
    # 출력 
    return cnt

'''
(1) 투 포인터(two-pointer)(슬라이딩 윈도우 방식)
- 시간 복잡도 O(n²) -> O(n) 
- 기존 모든 1부터 n까지 모든 숫자에서 합을 하나씩 확인하는 방식에서 불필요한 덧셈 반복을 제거한 방식


## 이전 통과 코드
def solution(n):
    # 변수 정의
    cnt = 0 
    # 연속하는 자연수로 n이 표현되는 경우의 수
    for i in range(1, n+1):
        sum = 0 
        num = i
        
        while sum < n:
            sum += num 
            num += 1
        
        if sum == n:
            cnt += 1
    # 출력
    return cnt
    
'''