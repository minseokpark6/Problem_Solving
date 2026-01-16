from itertools import combinations
import math 

def is_prime(n):
    if n < 2:
        return False 
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True
    

def solution(nums):
    # 변수 정의
    cnt = 0
    
    # 소수 개수 카운트 
    for a, b, c in combinations(nums, 3):
        if is_prime(a+b+c):
            cnt += 1
    
    # 출력
    return cnt

'''
## 개선점
(1) 소수 판별 속도 개선
- 불필요한 숫자까지 모두 돌아가지 않게 소수 판별 범위 축소
(2) 불필요한 메모리 사용 개선
- sums 리스트 삭제 


## 이전 코드
from itertools import combinations as comb

def solution(nums):
    # 변수 정의 
    answer = []
    # 서로 다른 3개의 숫자를 골라 더한 값의 리스트 생성 
    sums = [sum(c) for c in comb(nums, 3)]
    
    # 소수 개수 카운트 
    for n in sums:
        if all(n % i != 0 for i in range(2, n)):
            answer.append(n)
                
    return len(answer)
        

    

# combinations 
- itertools 모듈에 포함되어 있는 함수
- 주어진 iterable에서 순서를 고려하지 않고 특정 길이의 모든 조합을 생성하는 데 사용
- 조합을 나타내는 튜플을 반환
'''