from collections import deque
# 입력
n = int(input())
q = deque([i for i in range(1, n+1)])

# 제일 마지막에 남게 되는 카드 구하기 
while len(q)>1:
    # 제일 위에 있는 카드 버리기
    q.popleft()
    # 제일 위에 있는 카드를 아래로 옮기기
    if len(q) > 1:
        q.rotate(-1)

# 출력 
print(q.pop())