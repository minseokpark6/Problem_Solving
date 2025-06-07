import sys
from collections import deque
input = sys.stdin.readline 
# 입력
n = int(input().strip())
# 명령 입력
q = deque()
for _ in range(n):
    command = input().strip()
    if 'push' in command:
        num = int(command.split()[1])
        q.append(num)
    elif command == 'pop':
        print(q.popleft() if q else -1)
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        print(0 if q else 1)
    elif command == 'front':
        print(q[0] if q else -1)
    elif command == 'back':
        print(q[-1] if q else -1)