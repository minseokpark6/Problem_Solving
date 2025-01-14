def solution(arr1, arr2):
    # 변수 정의
    answer = []
    
    # 행렬의 곱셈
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2[0])):
            a = 0
            for k in range(len(arr2)):        # 행렬의 곱은 arr1의 열의 개수와 arr2의 행의 개수가 같아야 가능
                a += arr1[i][k] * arr2[k][j]
            temp.append(a)
        answer.append(temp)

    # 출력
    return answer
