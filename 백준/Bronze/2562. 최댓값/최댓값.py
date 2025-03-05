arr = []
for _ in range(9):
    arr.append(int(input()))
answer = max(arr)
print(answer)
print(arr.index(answer)+1)