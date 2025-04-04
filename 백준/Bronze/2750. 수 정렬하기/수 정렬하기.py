n = int(input())
arr = sorted([int(input()) for _ in range(n)])
# 출력 
print(*arr, sep="\n")