import sys
import math
input = sys.stdin.readline
# 입력 
n = int(input().strip())
# 나무 위치 입력
trees = [int(input().strip()) for _ in range(n)]
# 나무 사이 공간 및 공간의 최대 공약수 
space = [trees[idx]-trees[idx-1] for idx in range(1, n)]
gcd = math.gcd(*space)
# 현재 있는 나무의 개수 + 심어야하는 나무의 개수 
total = ((trees[-1]-trees[0])//gcd)+1
# 심어야하는 나무 숫자 출력
print(total-n)