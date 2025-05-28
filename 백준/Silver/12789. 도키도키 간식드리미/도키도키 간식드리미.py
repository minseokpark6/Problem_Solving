from collections import deque
# 입력
n = int(input())
students = deque(list(map(int, input().split())))
stack = deque()
# 간식 배부
turn_no = 1
for stu in students:
    # stack으로 줄 세우기
    stack.append(stu)
    # stack에서 순서 확인
    while stack and stack[-1]==turn_no:
        stack.pop()
        turn_no += 1

# 출력
print("Nice" if not stack else "Sad")