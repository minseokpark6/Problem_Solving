import sys
input = sys.stdin.readline
# 입력 
k = int(input())
# 재민이가 적어낸 모든 수의 합 
stack = []
for _ in range(k):
    num = int(input())
    if stack and num==0:
        stack.pop()
    else:
        stack.append(num)
# 출력 
print(sum(stack))