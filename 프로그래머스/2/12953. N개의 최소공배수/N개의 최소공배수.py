import math

def solution(arr):
    
    while len(arr) >= 2:
        # 배열 내 왼쪽 두 수 선택
        a, b = arr[0], arr[1]
        # 최소 공배수 배열에 추가
        arr.append(a*b // math.gcd(a, b))
        # 구한 숫자 제거 
        arr = arr[2:]

    # 출력
    return arr[0]

"""
# 모든 수의 최소 공배수를 한 번에 구하는 것이 아니라 
두 수의 최소 공배수를 리스트에 추가하여, 모든 수의 최소공배수를 구하는 방식으로

"""