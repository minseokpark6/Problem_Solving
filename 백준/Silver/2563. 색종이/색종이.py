n = int(input())    # 색종이 개수 입력 
arr = [[0]*100 for _ in range(100)]    # 100*100의 2차원 배열 생성
# 색종이가 차지하는 부분을 1로 표기
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
# 색종이 넓이 카운트
cnt = 0
for i in range(100):
    cnt += arr[i].count(1)
# 출력
print(cnt)