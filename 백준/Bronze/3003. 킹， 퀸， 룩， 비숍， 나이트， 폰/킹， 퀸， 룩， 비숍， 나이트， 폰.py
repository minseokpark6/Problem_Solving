ori = [1, 1, 2, 2, 2, 8]
c = [int(i) for i in input().split()]
answer = []
for idx in range(len(ori)):
    answer.append((ori[idx]-c[idx]))
for i in range(len(answer)):
    print(answer[i], end= ' ')