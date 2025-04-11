import sys
input = sys.stdin.readline
# 가입한 사람 명수 입력
n = int(input())
# 가입한 사람 명단 입력 및 정렬
arr = sorted([input().split() for _ in range(n)], key = lambda x: int(x[0]))
# 출력
for i in arr:
    print(" ".join(i))