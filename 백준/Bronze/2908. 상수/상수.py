temp = input().split()
arr = [int(i[::-1]) for i in temp]
print(max(arr))