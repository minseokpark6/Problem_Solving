from itertools import combinations

def solution(numbers):
    return sorted(set(sum(c) for c in combinations(numbers, 2)))

'''
## 이전 통과 코드 

def solution(numbers):
    # 변수 지정
    answer = []
    
    # 두 수의 합 모두 구하기
    for idx in range(len(numbers)):
        temp = [num for i, num in enumerate(numbers) if i != idx] 
        for num in temp:
            answer.append(numbers[idx] + num)
    
    # 중복 제거 후 반환
    return sorted(set(answer))

'''