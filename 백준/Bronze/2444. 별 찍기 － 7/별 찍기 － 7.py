n = int(input())

# 위쪽 삼각형
for i in range(1, n+1):
    print(f'{" " * (n-i)}{"*" * (2*i - 1)}')

# 아래쪽 삼각형
for j in range(n-1, 0, -1):
    print(f'{" " * (n-j)}{"*" * (2*j - 1)}')