def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]


'''
## 이전 통과 코드

def solution(array, commands):
    # 변수 정의 
    answer = []
    
    # 연산 적용한 결과 배열에 담기 
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        answer.append(sorted(array[i-1:j])[k-1])
    
    # 출력
    return answer
'''