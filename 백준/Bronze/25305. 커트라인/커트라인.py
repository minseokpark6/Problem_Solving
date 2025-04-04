# 입력
n, k = map(int, input().split())
arr = sorted([int(i) for i in input().split()], reverse=True)
# 출력
print(arr[k-1])