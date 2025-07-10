from collections import deque
import sys
input = sys.stdin.readline

# 입력
N = int(input())                      # 자료 구조의 개수 N
A = list(map(int, input().split()))   # 자료구조를 나타내는 수열 A
B = list(map(int, input().split()))   # 각 자료 구조의 원소 값 수열 B
M = int(input())                      # 삽입할 원소의 길이를 나타내는 M
C = list(map(int, input().split()))   # 삽입할 원소의 수열 C

# 자료구조가 queue인 원소만 남긴 배열
q = deque()
for i in range(N):
    if A[i] == 0:
        q.append(B[i])

# 배열 C의 원소를 appendleft할 때마다 원소를 pop하여 출력 
for i in range(M):
    q.appendleft(C[i])
    print(q.pop(), end = " ") 