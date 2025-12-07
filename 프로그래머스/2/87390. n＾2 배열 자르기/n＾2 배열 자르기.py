def solution(n, left, right):
    return [max(i%n, i//n) + 1 for i in range(left, right+1)]

'''
## 개선한 부분 
(1) 기존 코드가 해당 문제에서는 최적의 성능을 가지고 있었기 때문에 리스트 컴프리헨션으로만 변경

## 이전 통과 코드 

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

## 좌표값 구하기 

#1
n = 3
[[1,2,3], [2,2,3], [3,3,3]]

(0, 0), (1, 0), (2, 0) / (0, 1), (1, 1), (2, 1) / (0, 2), (1, 2), (2, 2)
0        1         2        3       4       5        6       7       8

좌표 중 큰 값을 구한 후 +1 하면 해당 좌표값 


#2
n=4
[[1,2,3,4], [2,2,3,4], [3,3,3,4], [4,4,4,4]]

'''