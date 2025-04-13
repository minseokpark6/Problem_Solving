import sys
input = sys.stdin.readline
# 입력
n = int(input())
people = set()
# 현재 회사에 있는 사람
for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        people.add(name)
    else:
        people.remove(name)
# 역순으로 출력
for name in sorted(people, reverse=True):
    print(name)