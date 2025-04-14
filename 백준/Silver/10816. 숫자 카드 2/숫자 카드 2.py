import sys 
input = sys.stdin.readline 
# 입력 
n = int(input())
# 상근이가 가지고 있는 카드 
card = {}
for i in list(map(int, input().split())):
    if i in card:
        card[i] += 1
    else:
        card[i] = 1
# 주어진 카드 
m = int(input())
arr = [card[i] if i in card else 0 for i in list(map(int, input().split()))]
# 출력 
print(*arr)