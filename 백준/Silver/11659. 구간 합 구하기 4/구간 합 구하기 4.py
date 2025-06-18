import sys 
input = sys.stdin.readline 
# 입력 
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 배열 생성
prefix_sum = [0]
for num in arr:
    prefix_sum.append(prefix_sum[-1] + num)
    
# 구간합 출력 
for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])