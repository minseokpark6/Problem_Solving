# (1) 입력
n, k = map(int, input().split())
arr = list(map(int, input().split()))
# (2) 연속적인 K일 온도의 합 배열 구하기 
num = sum(arr[:k]) # 첫 k일의 온도의 합 
max_num = num
# 다음 k일의 온도의 합 담기
for idx in range(n-k):
    num -= arr[idx]
    num += arr[idx+k]
    max_num = max(max_num, num)
# (3) 최대값 출력 
print(max_num)