# 입력
n = int(input())
# 생성자 찾기
temp = 1
while temp < n:
    g_num = temp + sum(map(int, str(temp)))
    if g_num == n:
        print(temp)
        break
    temp += 1
else:  # 생성자가 없는 경우
    print(0)