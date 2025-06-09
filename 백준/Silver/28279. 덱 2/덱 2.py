import sys 
from collections import deque 
input = sys.stdin.readline
# 입력 
n = int(input().strip())
q = deque()
# 명령에 따른 출력
for _ in range(n):
    command = list(map(int, input().strip().split()))
    if command[0] == 1:
        q.appendleft(command[1])
    elif command[0] == 2:
        q.append(command[1])
    if command[0] == 3:
        print(q.popleft() if q else -1)
    elif command[0] == 4:
        print(q.pop() if q else -1)
    elif command[0] == 5:
        print(len(q))
    elif command[0] == 6:
        print(0 if q else 1)
    elif command[0] == 7:
        print(q[0] if q else -1)
    elif command[0] == 8:
        print(q[-1] if q else -1)