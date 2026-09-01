def solution(my_string):
    # 변수 정의
    arr = my_string.split()
    result = int(arr[0])

    # 계산하기
    for i in range(1, len(arr), 2):
        if arr[i] == "-":
            result -= int(arr[i+1])
        else:
            result += int(arr[i+1])

    # 출력
    return result



'''
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
'''