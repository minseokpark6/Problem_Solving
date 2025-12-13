def solution(arr1, arr2):
    # 변수 정의
    result = []
    arr2_col = list(zip(*arr2))    # arr2를 열 기준 리스트로 변환(전치 행렬)
     
    # 행렬의 곱셈
    for row in arr1:
        temp = []
        for col in arr2_col:
            temp.append(sum(r*c for r, c in zip(row, col)))
        # 출력
        result.append(temp)

    # 출력
    return result



'''
## 개선점
(1) 전치행렬을 활용하여 for문을 3개에서 2개로 축소 
-> 시간 복잡도 개선 
(2) 복잡한 인덱스 접근을 최소화


## 기존 통과 코드
def solution(arr1, arr2):
    # 변수 정의 
    result = []
    
    # 행렬의 곱셈 
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2[0])):
            n = 0
            for k in range(len(arr2)):      # 행렬의 곱은 arr1의 열의 개수와 arr2의 행의 개수가 같아야 가능
                n += arr1[i][k] * arr2[k][j]
                
            temp.append(n)
        result.append(temp)
    
    # 출력
    return result

'''