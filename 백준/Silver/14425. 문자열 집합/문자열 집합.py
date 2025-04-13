import sys
input = sys.stdin.readline
# 입력 
n, m = map(int, input().split())
s = set([input().strip() for _ in range(n)])
# M개의 문자열 중 s 집합에 포함되어 있는 단어의 개수(코드 간소화)
print(sum(1 for _ in range(m) if input().strip() in s))