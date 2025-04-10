# 입력
n = int(input())
# 정렬
arr = sorted([input().split() for _ in range(n)], key = lambda x:(int(x[1]), int(x[0])))
# 출력
for dot in arr:
    print(dot[0], dot[1])