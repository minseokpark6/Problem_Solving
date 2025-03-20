n = int(input())
cnt, temp = 1, 1
while n > temp:
    temp += (6*cnt)
    cnt += 1
print(cnt)