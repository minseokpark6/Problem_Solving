s = input()
al = 'abcdefghijklmnopqrstuvwxyz'

for i in al:
    if i in s:
        print(s.index(i), end = " ")
    else:
        print(-1, end = " ")