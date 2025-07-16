def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
        return 
    # 위에 있는 n-1개의 원판을 mid로 옮김
    hanoi(n-1, start, end, mid)
    # 그리고 가장 밑에 있는 큰 원판을 end로 옮김 
    print(start, end)
    # 그 후 mid에 있는 n-1 원판을 end로 옮김
    hanoi(n-1, mid, start, end)

# 입력 
n = int(input())

# 출력
# 하노이 탑 이동 횟수 출력
print((2**n)-1)
# 이동 경로 출력 
hanoi(n, 1, 2, 3)