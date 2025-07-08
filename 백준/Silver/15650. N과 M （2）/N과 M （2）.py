# 조합(combination) 백트래킹 함수 지정 
def backtrack(start, result):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(start, n+1):
        result.append(i)
        backtrack(i+1, result)
        result.pop()
        
# 입력
n, m = map(int, input().split())

# 출력 >> start 값 지정
backtrack(1, []) 


'''
from itertools import combinations
# 입력 
n, m = map(int, input().split())
# 주어진 수 리스트 구하기 
arr = [i for i in range(1, n+1)]
# 출력
for i in combinations(arr, m):
    print(*i)
'''