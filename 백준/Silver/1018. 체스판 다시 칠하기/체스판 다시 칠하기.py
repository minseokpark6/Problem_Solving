# 입력 
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

# 체스판 다시 칠하는 최소 횟수 카운트 함수
def count_repaint(x, y):
    repaint1 = 0 # 시작이 'W'인 경우
    repaint2 = 0 # 시작이 'B'인 경우
    
    for i in range(8):
        for j in range(8):
            current = board[x + i][y + j]
            # 체스판의 정답 패턴: (i+j)%2==0 → 시작 색, (i+j)%2==1 → 반대 색
            if (i + j) % 2 == 0:  # 시작 색
                if current != 'W':  # 시작이 W라고 가정
                    repaint1 += 1
                if current != 'B':  # 시작이 B라고 가정
                    repaint2 += 1
            else:  # 반대 색
                if current != 'B':  # 시작이 W라고 가정
                    repaint1 += 1
                if current != 'W':  # 시작이 B라고 가정
                    repaint2 += 1

    return min(repaint1, repaint2)

# 가장 큰 값으로 초기화
min_repaint = float('inf')

# 전체 보드 탐색하여 최소값 찾기
for i in range(n - 7): # 8행씩만 확인 가능
    for j in range(m - 7): # 8열씩만 확인 가능
        repaint = count_repaint(i, j)
        min_repaint = min(min_repaint, repaint)

# 출력
print(min_repaint)