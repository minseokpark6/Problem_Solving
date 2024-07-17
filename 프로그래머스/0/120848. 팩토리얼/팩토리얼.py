def solution(n):
    answer = 0
    while True:
        answer += 1
        temp = 1
        for i in range(1, answer+1):
            temp *= i
        
        if temp < n :
            continue
        elif temp == n:
            return answer
            break
        else:
            return answer - 1
            break
        
    