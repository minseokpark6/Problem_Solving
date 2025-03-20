t = int(input())
changes = [25, 10, 5, 1] # 쿼터, 다임, 니켈, 페니

for _ in range(t):
    c = int(input())
    res = []
    for i in changes:
        res.append(c//i)
        c = c%i
        
    print(*res)