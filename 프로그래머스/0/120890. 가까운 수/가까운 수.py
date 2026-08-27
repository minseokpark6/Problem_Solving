def solution(array, n):
    # 정수 n과의 거리
    diff = {i:abs(i-n) for i in array}
    # 출력
    return sorted(diff.items(), key= lambda x:(x[1], x[0]))[0][0]


'''
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
'''