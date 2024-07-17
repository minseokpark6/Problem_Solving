def solution(array, n):
    answer = array[0]
    temp = abs(array[0] - n)
    for i in array:
        if temp > abs(i - n):
            answer = i
            temp = abs(i - n)
        elif temp == abs(i - n):
            if answer > i:
                answer = i 
            else :
                continue
            
    return answer