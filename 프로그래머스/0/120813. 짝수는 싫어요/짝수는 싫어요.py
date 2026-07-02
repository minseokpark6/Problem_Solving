def solution(n):
    return [i for i in range(n+1) if i%2==1]



''' 
## 이전 통과 코드

def solution(n):
    answer = []
    if n % 2 == 0:
        for i in range(1, n, 2):
            answer.append(i)  
    else :
        for i in range(1, n+1, 2):
            answer.append(i)
    return answer

'''