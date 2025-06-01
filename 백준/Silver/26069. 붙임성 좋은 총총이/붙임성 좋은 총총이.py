import sys 
input = sys.stdin.readline
# 입력 
n = int(input())
# 총총이를 만나 무지개 댄스를 추는 사람의 수 구하기 
arr = set()
arr.add('ChongChong')
for _ in range(n):
    a, b = map(str, input().split())
    if a in arr:
        arr.add(b)
    elif b in arr:
        arr.add(a)
# 출력 
print(len(arr))