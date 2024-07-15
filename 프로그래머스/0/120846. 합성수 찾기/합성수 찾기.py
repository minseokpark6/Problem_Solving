def solution(n):
    answer = []
    temp = []
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                temp.append(i)
            
        if len(temp) >= 3:
            answer.append(i)
        temp = []
    
    return len(answer)