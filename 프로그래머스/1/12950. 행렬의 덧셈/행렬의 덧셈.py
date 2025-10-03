def solution(arr1, arr2):
    # 행렬의 덧셈 출력
    return [[a + b for a, b in zip(i, j)] for i, j in zip(arr1, arr2)]

'''
# 변수 지정 
answer = []
# 행렬의 덧셈 계산 연산 
for i, j in zip(arr1, arr2):
    row = []
    for a, b in zip(i, j):
        row.append(a+b)
    answer.append(row)
    
print(answer)

## 기존 코드 

for i, j in zip(arr1, arr2):
    temp = []
    for idx in range(len(i)):
        temp.append(i[idx]+j[idx])
    answer.append(temp)
'''