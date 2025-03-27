# 입력
n, k = map(int, input().split())
# n의 약수 리스트 생성
arr = [i for i in range(1, n+1) if n%i==0]
# 출력
if len(arr) >= k:
    print(arr[k-1])
else:
    print(0)