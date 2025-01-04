def solution(arr1, arr2):
    # 변수 정의 
    answer = []
    
    # 행렬의 덧셈 결과 구하기 
    for i, j in zip(arr1, arr2):
        temp = []
        for idx in range(len(i)):
            temp.append(i[idx]+j[idx])
        answer.append(temp)
        
    # 출력
    return answer