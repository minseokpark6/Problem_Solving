# 입력
m = int(input())
n = int(input())
# 소수 리스트
arr = []
for i in range(m,n+1):
    e=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                e+=1
                break
        if e==0:
            arr.append(i)
# 출력
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)