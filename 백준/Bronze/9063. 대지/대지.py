# 점의 개수 입력
n = int(input())
# 모든 점 리스트 생성
X, Y = zip(*(map(int, input().split()) for _ in range(n)))
# 넓이 출력
print((max(X)-min(X))*(max(Y)-min(Y)))