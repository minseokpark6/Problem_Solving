n, x = map(int, input().split())
arr = input().split()
print(" ".join(i for i in arr if int(i) < x))
