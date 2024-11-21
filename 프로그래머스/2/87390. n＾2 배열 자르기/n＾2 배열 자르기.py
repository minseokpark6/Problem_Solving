def solution(n, left, right):
    # 빈 리스트 생성
    answer = []
    
    # left, right를 활용하여 좌표를 구한 후, 리스트에 해당 좌표값 추가
    for i in range(left, right+1):
        x, y = i%n, i//n
        num = max(x, y) + 1
        answer.append(num)

    # 출력 
    return answer


"""
#1
n = 3
[[1,2,3], [2,2,3], [3,3,3]]

(0, 0), (1, 0), (2, 0) / (0, 1), (1, 1), (2, 1) / (0, 2), (1, 2), (2, 2)
0        1         2        3       4       5        6       7       8

좌표 중 큰 값을 구한 후 +1 하면 해당 좌표값 


#2
n=4
[[1,2,3,4], [2,2,3,4], [3,3,3,4], [4,4,4,4]]

"""


"""
# 시간 초과 실패 

def solution(n, left, right):
    # 빈 리스트 생성
    result = []
    
    # 2차원 배열 생성
    for i in range(n):
        # 임시 리스트 생성
        temp = []
        for j in range(i, n):
            temp.append(j+1)
            if temp.index(j+1) != j:
                temp *= (j+1)
                
        # 리스트에 임시 리스트 추가
        result.append(temp)
        
    # 1차원화 
    answer = [num for num_list in result for num in num_list]

    # 출력 
    return answer[left:right+1]
"""
