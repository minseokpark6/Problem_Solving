def solution(n):
    answer = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    return answer


"""
def solution(n):
    answer = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                answer[i][j] = 1
    return answer
"""


"""
answer = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    answer.append(row)
"""