# 입력 
n = int(input())    # 수의 개수
arr = list(map(int, input().split()))   # 주어진 수열
oper = list(map(int, input().split()))  # 주어진 연산자의 개수

# 최대값, 최소값 기본값 설정 
maximum = -1e9  # 가장 작은 값으로
minimum = 1e9   # 가장 큰 값으로

# 백트래킹 함수 설정 
def dfs(depth, total, plus, minus, multifly, divide):
    global maximum, minimum 
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        
    if plus:
        dfs(depth+1, total+arr[depth], plus-1, minus, multifly, divide)
    if minus:
        dfs(depth+1, total-arr[depth], plus, minus-1, multifly, divide)
    if multifly:
        dfs(depth+1, total*arr[depth], plus, minus, multifly-1, divide)
    if divide:
        dfs(depth+1, int(total/arr[depth]), plus, minus, multifly, divide-1)

# 출력
dfs(1, arr[0], oper[0], oper[1], oper[2], oper[3])
print(maximum)
print(minimum)