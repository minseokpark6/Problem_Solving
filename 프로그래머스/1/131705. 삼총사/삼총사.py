from itertools import combinations

def solution(number):
    return sum(1 for triple in combinations(number, 3) if sum(triple)==0)


'''
(1) 리스트 컴프리헨션 vs 제너레이터 표현식 
- 리스트 컴프리헨션 + count 는 불필요한 메모리 사용 및 중복 순회 발생 
- 제너레이터 표현식 + sum()을 쓰면 한 번의 루프로 카운트 가능

## 기존 코드
def solution(number):
    # 주어진 리스트에서 세 개 수의 조합 리스트 
    result = [sum(c) for c in comb(number, 3)]
    # 0의 개수 카운트 
    answer = result.count(0)
    # 출력
    return answer


# combinations 
- itertools 모듈에 포함되어 있는 함수
- 주어진 iterable에서 순서를 고려하지 않고 특정 길이의 모든 조합을 생성하는 데 사용
- 조합을 나타내는 튜플을 반환

'''