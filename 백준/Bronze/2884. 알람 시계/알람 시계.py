h, m = map(int, input().split())
if (m-45) < 0:
    m += 15
    if h != 0:
        h -= 1
    else:
        h = 23
    print(h, m)
else:
    print(h, m-45)

    