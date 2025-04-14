import sys 
input = sys.stdin.readline 
# 입력 
n, m = map(int, input().split())
# 두 집합 
arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))
# 대칭 차집합의 개수 구하기 
print(len((arr1-arr2)|(arr2-arr1)))