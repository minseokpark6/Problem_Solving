from collections import deque 

# 입력 
n = int(input())
q = deque(enumerate(map(int, input().split())))

# 풍선 터뜨리기
arr = []
while q:
    idx, now_turn = q.popleft()
    arr.append(idx+1)
    
    if now_turn > 0:
        q.rotate(-(now_turn-1))
    else:
        q.rotate(-now_turn)
    
# 출력
print(*arr, sep=" ")