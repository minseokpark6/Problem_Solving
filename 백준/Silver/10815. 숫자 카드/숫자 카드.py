# 입력
n = int(input())
card = set(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
# 숫자 카드 소유 여부 
answer = [1 if num in card else 0 for num in arr]
# 출력 
print(*answer)