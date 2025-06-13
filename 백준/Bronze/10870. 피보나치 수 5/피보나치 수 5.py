# 재귀함수 설정
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# 입력
n = int(input())
# 출력
print(fibonacci(n))