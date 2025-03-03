price = int(input())
cnt = int(input())
total = 0

for _ in range(cnt):
    pro, n = map(int, input().split())
    total += pro*n

print("Yes") if price == total else print("No")