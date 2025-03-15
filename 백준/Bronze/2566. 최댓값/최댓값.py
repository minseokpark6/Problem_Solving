l, r, m = 0, 0, 0   # 행, 열, 최대값 변수
max_line = 1
for _ in range(9):
    arr = [int(i) for i in input().split()]
    l += 1
    temp = max(arr)
    if m < temp:
        max_line, r, m = l, arr.index(temp), temp
print(m)
print(max_line, r+1)