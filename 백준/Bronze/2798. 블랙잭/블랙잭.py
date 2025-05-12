from itertools import combinations
import sys 
input = sys.stdin.readline
# 입력 
n, m = map(int, input().split())
cards = list(map(int, input().split())) 
# 모든 경우의 수 구하기 
comb = list(combinations(cards, 3))
arr = [sum(c) for c in comb]
# m에 가장 가까운 수 구하기 
answer = 0
for i in arr:
    if i > m:
        continue
    if i > answer:
        answer = i 
# 출력
print(answer)