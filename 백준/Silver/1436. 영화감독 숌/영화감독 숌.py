# 입력
n = int(input())
# 변수 지정 
result, cnt = 666, 0
# n번째 수 찾기 
while True:
    if '666' in str(result):
        cnt += 1
    if cnt == n:
        print(result)
        break
    result += 1