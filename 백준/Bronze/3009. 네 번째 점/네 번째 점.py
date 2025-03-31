# x, y 좌표 각각 리스트 생성
X, Y = zip(*(map(int, input().split()) for _ in range(3)))
# 개수가 1개인 각 좌표 찾기
for i in range(3):
    if X.count(X[i])==1:
        x=X[i]
    if Y.count(Y[i])==1:
        y=Y[i]
# 출력
print(x, y)