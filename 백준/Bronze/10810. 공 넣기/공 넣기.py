n, m = map(int, input().split())
baskets = [0] * (n+1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        baskets[x] = k

for i in range(1, len(baskets)):
    print(baskets[i], end=' ')
