def solution(my_string):
    sum = 0
    temp = my_string.split(" ")
    answer = []
    for idx, num in enumerate(temp):
        if num == "-":
            temp[idx+1] = -(int(temp[idx+1]))
        elif num == "+":
            temp[idx+1] = int(temp[idx+1])
        else:
            answer.append(int(num))
    for i in answer:
        sum += i
    return sum