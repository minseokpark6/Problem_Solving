n = int(input())
for _ in range(n):
    answer = ""
    cnt, s = map(str, input().split())
    for i in s:
        answer += (i*int(cnt))
    print(answer)