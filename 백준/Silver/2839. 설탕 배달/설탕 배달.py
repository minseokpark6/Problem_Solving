n = int(input())
arr = []

# (1) 5로 먼저 나누기
for i in range(1, (n//5)+1):
    total_cnt, res = i, n-(5*i)
    if res == 0:
        arr.append(total_cnt)
    # 5로 나누어 떨어지지 않는 수일 경우
    else:
        cnt, res = res//3, res%3
        total_cnt += cnt 
        if res == 0:
            arr.append(total_cnt)

# (2) 3으로만 나누기 
total_cnt, res = n//3, n%3
if res == 0:
    arr.append(total_cnt)

# 출력 
print(min(arr) if arr else -1)