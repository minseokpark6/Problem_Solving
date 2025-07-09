# 백트래킹 함수 지정 
def backtrack(result):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(1, n+1):
        result.append(i)
        backtrack(result)
        result.pop()
        
# 입력
n, m = map(int, input().split())

# 출력 >> start 값 지정
backtrack([])