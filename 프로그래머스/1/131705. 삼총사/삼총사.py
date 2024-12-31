from itertools import combinations as comb

def solution(number):
    # 주어진 리스트에서 세 개 수의 조합 리스트 
    result = [sum(c) for c in comb(number, 3)]
    # 0의 개수 카운트 
    answer = result.count(0)
    # 출력
    return answer


"""
# combinations 
- itertools 모듈에 포함되어 있는 함수
- 주어진 iterable에서 순서를 고려하지 않고 특정 길이의 모든 조합을 생성하는 데 사용
- 조합을 나타내는 튜플을 반환
"""