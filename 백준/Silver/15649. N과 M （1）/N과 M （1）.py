from itertools import permutations
# 입력 
n, m = map(int, input().split())
# 주어진 수 리스트 구하기 
arr = [i for i in range(1, n+1)]
# 출력
for i in permutations(arr, m):
    print(*i)