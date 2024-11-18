def solution(n):
    # n이 0 -> 1로 이동하려면 배터리 사용 한 번 해야함  
    ans = 1
    
    while n > 1:
        # 짝수일 때는 순간이동
        if n % 2 == 0:
            n //= 2
        # 홀수 일때는 순간이동 불가능하니까 배터리 사용
        else:
            n -= 1
            ans += 1

    # 출력
    return ans

'''
## 목적지에 도착한 과정을 거꾸로 한다고 생각
순간이동은 나누기 2
건전지 사용은 -1

## ex.
5000 / 2 = 2500
2500 / 2 = 1250
1250 / 2 = 625

-1

624 / 2 = 312
312 / 2 = 106
106 / 2 = 53

-1

52 / 2 = 26
26 / 2 = 13

-1

12 / 2 = 6
6 / 2 = 3

-1

2 / 2 = 1

-1

'''