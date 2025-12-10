import math 

# 약수의 개수를 구하는 함수 정의 
def attack_cnt(num):
    # 변수 정의
    cnt = 0
    root = math.isqrt(num)
    # 약수의 개수 카운트
    for n in range(1, root+1):
        if n ** 2 == num:
            cnt += 1
        elif num % n == 0:
            cnt += 2
    # 출력
    return cnt

# 철의 무게 구하는 함수 정의
def solution(number, limit, power):
    # 변수 정의 
    total = 0 
    
    # 철의 무게 구하기 
    for i in range(1, number+1):
        cnt = attack_cnt(i)
        total += power if cnt > limit else cnt 
        
    # 출력
    return total

'''
## 개선점 
(1) solution 함수에서 attack_cnt 함수를 두 번 호출하는 형태 개선
(2) int(num**0.5) 부동소수점에서 오는 정확성에서의 문제 개선
- 매우 큰 수에서는 이론적으로 k가 나와야할 제곱근이 k-1이 나올 경우도 존재 
- 이론적이기는 하지만 발생할 수도 있는 오류이기 때문에 사전에 차단하는 것이 좋음
- 따라서 제곱근을 사용할 경우에는 부동소수점 보다는 math.isqrt()를 사용하는 것을 권장 

## 이전 통과 코드 

# 약수의 개수 구하는 함수 정의
def attack_cnt(num):
    cnt = 0
    for n in range(1, int(num**0.5)+1):
        if n ** 2 == num:
            cnt += 1
        elif num % n == 0:
            cnt += 2
    return cnt

# 철의 무게 구하기 
def solution(number, limit, power):
    return sum(power if attack_cnt(i) > limit else attack_cnt(i)  for i in range(1, number+1))


## 약수를 구할 때 시간 복잡도를 줄이는 방법 
-> n의 약수를 구할 때 약수는 항상 짝지어 나온다는 것을 생각하면 
- 아래 실패한 방법의 시간 복잡도 : O(N)
- 위 방법의 시간 복잡도 :  O(N^(1/2))

## 시간초과 실패 코드 
def solution(number, limit, power):
    # 기사 별 약수의 개수 저장
    attack = []
    for i in range(1, number+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count+=1

        # 공격력 제한 수치 확인 후 리스트에 추가
        if count > limit:
            count = power
        attack.append(count)

    # 출력
    return sum(attack)

'''