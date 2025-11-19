import math 
from functools import reduce 

def solution(arr):
    return reduce(lambda a, b: a * b // math.gcd(a,b), arr) if len(arr) >= 2 else arr[0]

'''
(1) reduce
- reduce(func, iterable)
- iterable의 원소들을 차례로 func에 적용해 하나의 값으로 누적(reduce) 하는 함수 
- 길이가 0일 때는 TypeError 발생 
- 길이가 1일 때는 함수에 적용할 다음 값이 없으므로, 초기값 반환 

## 위의 코드를 람다 대신 가독성 있게 쓴 코드 ver.

import math
from functools import reduce

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    return reduce(lcm, arr, 1)  # 초기값 1을 주면 빈 리스트도 안전 처리


## 2차 통과 코드 

import math

def solution(arr):
    # 변수 지정 
    lcm = arr[0]

    # N개의 최소공배수 찾기
    if len(arr)>=2:
        for num in arr[1:]:
            lcm = lcm * num // math.gcd(lcm, num)
    
    # 출력
    return lcm
        


(1) 매 반복마다 리스트 슬라이싱을 할 경우 성능이 좋지 않음 
- 리스트 슬라이싱은 O(n)

(2) 주어진 리스트를 계속 바꾸는 것 보다 누적 변수로 처리하는 것이 깔끔 


## 기존 통과 코드 


import math 

def solution(arr):
    
    # n개의 수의 최소 공배수 구하기 
    while len(arr)>=2:
        # 배열 내 왼쪽 두 개의 수 선택 
        a, b = arr[0], arr[1]
        
        # 두 수의 최소 공배수 배열에 추가
        arr.append(a*b//math.gcd(a, b))
        
        # 구한 숫자 제거 
        arr = arr[2:]
    
    # 출력
    return arr[0]
'''