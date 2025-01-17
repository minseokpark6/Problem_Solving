from itertools import permutations

def solution(k, dungeons):
    # 최대 탐험 횟수
    max_cnt = 0
    # dungeons에서 순열을 구해 최대 탐험 횟수 구하기 
    for dungeon in permutations(dungeons):
        # 변수 정의
        cnt, fatigue = 0, k
        # 해당 순열에서의 탐험횟수 카운트
        for i, j in dungeon:
            if fatigue >= i:
                fatigue -= j
                cnt += 1
        # 최대 탐험 횟수와 비교 
        if max_cnt < cnt:
            max_cnt = cnt
    # 출력
    return max_cnt


'''
# 1) permutations: 순열
- 서로 다른 n개의 원소 중 r개를 골라 나열하는 가짓수 >> 순서를 고려

from itertools import permutations

arr = ['A', 'B', 'C']
nPr = permutations(arr, 2)
print(list(nPr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]


# 2) combinations: 조합
- 순서를 고려하지 않고, 원소를 골라 조합

from itertools import combinations

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]

'''