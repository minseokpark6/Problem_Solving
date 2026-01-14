def solution(numbers, target):
    def dfs(cnt, current_sum):
        # 정지 조건
        if cnt == len(numbers):
            # 타겟에 도달한 경우
            if current_sum == target:
                return 1
            # 도달하지 못한 경우
            else:
                return 0
            
        # 깊이 우선 탐색
        return dfs(cnt+1, current_sum + numbers[cnt]) + dfs(cnt+1, current_sum - numbers[cnt])

    # 탐색 시작 -> 출력
    return dfs(0, 0)


'''

## 이전 통과 코드 

from itertools import product

def solution(numbers, target):
    # 각 숫자에서 (+, -) 쌍으로 튜플 생성
    oper = [(i, -i) for i in numbers]
    
    # 더하고 뺄 수 있는 모든 경우의 수 생성 
    result = list(map(sum, product(*oper)))
    
    # 타켓 넘버 갯수 카운트 후 출력
    return result.count(target)
    

(1) itertools.product
- 여러 iterable(반복 가능한 객체)의 데카르트 곱(Cartesian product)을 구할 때 사용하는 유용한 함수
- 주어진 여러 iterable에서 각각 하나의 요소를 선택해 가능한 모든 조합을 만들어주는 함수

## 입력

from itertools import product

list1 = [1, 2]
list2 = ['A', 'B']

result = list(product(list1, list2))
print(result)


## 출력

[(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

'''