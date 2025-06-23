import sys 
input = sys.stdin.readline

# 입력 
s = input().strip()
q = int(input())

# 문자 횟수 카운트 
for _ in range(q):
    a, l, r = map(str, input().split())
    cnt = s.count(a, int(l), int(r)+1)
    print(cnt)