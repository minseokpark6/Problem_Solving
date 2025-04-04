import sys
# 입력
n = int(input())
arr = sorted([int(sys.stdin.readline()) for _ in range(n)])
# 출력
print(*arr, sep='\n')