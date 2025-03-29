n = int(input())
arr = [int(i) for i in input().split()]
cnt = 0
# 소수 개수 카운트
for i in arr:
    if i==1:
        continue
    temp = [j for j in range(1, i+1) if i%j==0]
    if len(temp) == 2:
        cnt += 1
# 출력
print(cnt)