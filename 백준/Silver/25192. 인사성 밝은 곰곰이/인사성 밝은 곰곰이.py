import sys
input = sys.stdin.readline
# 입력
n = int(input())
# 채팅 입력
cnt, arr = 0, set()
for _ in range(n):
    chat = input().strip()
    if chat == "ENTER":
        arr.clear()
    elif chat not in arr:
        cnt += 1
        arr.add(chat)
# 출력
print(cnt)