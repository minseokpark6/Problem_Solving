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
        

    
"""
# combinations 
- itertools 모듈에 포함되어 있는 함수
- 주어진 iterable에서 순서를 고려하지 않고 특정 길이의 모든 조합을 생성하는 데 사용
- 조합을 나타내는 튜플을 반환
"""