n, m = map(int, input().split())
bas = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    bas[i-1], bas[j-1] = bas[j-1], bas[i-1]

for i in range(len(bas)):
    print(bas[i], end=' ')