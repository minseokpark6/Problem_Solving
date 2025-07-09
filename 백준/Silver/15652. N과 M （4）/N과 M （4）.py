# 백트래킹 함수 지정 

def backtrack(start, result):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(start, n+1):
        result.append(i)
        backtrack(i, result)
        result.pop()
        
# 입력
n, m = map(int, input().split())

# 출력
backtrack(1, [])