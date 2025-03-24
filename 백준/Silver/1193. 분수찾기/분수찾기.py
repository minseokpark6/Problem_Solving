idx = int(input())
line = 1
# 해당 idx 값의 line 내 위치 찾기
while idx > line:
    idx -= line
    line += 1
# line 내 값 찾기
if line % 2 == 0:
    a = idx
    b = line-idx+1
else:
    a = line-idx+1
    b = idx
# 출력
print(f'{a}/{b}')