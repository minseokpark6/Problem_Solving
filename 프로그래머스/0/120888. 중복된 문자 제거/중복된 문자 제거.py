def solution(my_string):
    # 변수 정의
    arr = [i for i in my_string]
    result = []
    # 중복 문자열 제거 
    for s in arr:
        if s not in result:
            result.append(s)
    # 출력
    return "".join(result)

'''
def solution(my_string):
    answer = ''
    for i in my_string:
        if i in answer :
            continue
        else: 
            answer += i
    return answer
'''