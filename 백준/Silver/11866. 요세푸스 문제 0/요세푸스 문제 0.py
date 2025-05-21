from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n + 1)) # 1부터 n까지의 수를 덱으로

answer = []

while q:
    q.rotate(-(k - 1)) # 왼쪽으로 (k-1)칸 회전
    answer.append(q.popleft()) # k번째 사람 제거

print(f'<{", ".join(map(str, answer))}>')