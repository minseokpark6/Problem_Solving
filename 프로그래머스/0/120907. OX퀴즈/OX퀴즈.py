def solution(quiz):
    answer = []
    for i in quiz:
        temp = i.split(" ")
        if temp[1] == '-':
            temp[2] = -(int(temp[2]))
        sum = int(temp[0]) + int(temp[2])
        result = int(temp[4])
        
        if sum == result:
            answer.append("O")
        else:
            answer.append("X")
                     
    return answer