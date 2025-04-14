import sys 
input = sys.stdin.readline 
# 입력 
n, m = map(int, input().split())
# 듣도 / 보도 X 명단 
arr1 = set([input().strip() for _ in range(n)])
arr2 = set([input().strip() for _ in range(m)])
# 듣보잡 명단 >> 교집합 + 정렬
answer = sorted(arr1 & arr2)
# 출력 
print(len(answer))
print(*answer, sep='\n')