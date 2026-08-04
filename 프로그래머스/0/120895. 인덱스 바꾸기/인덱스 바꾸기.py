def solution(my_string, num1, num2):
    # 문자열 변환을 위해 리스트로 변경
    arr = list(my_string)
    # 인덱스 변환
    arr[num1], arr[num2] = arr[num2], arr[num1]
    # 출력 
    return "".join(arr)

'''
def solution(my_string, num1, num2):
    answer = my_string
    str1 = my_string[num1]
    str2 = my_string[num2]
    answer = list(answer)
    answer[num1] = str2
    answer[num2] = str1
    answer = ''.join(answer)
    return answer
'''