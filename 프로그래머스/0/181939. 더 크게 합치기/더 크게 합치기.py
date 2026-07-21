def solution(a, b):
    # 변수 정의
    r1, r2 = int(str(a)+str(b)), int(str(b)+str(a))
    # 츨력
    return r1 if r1 >= r2 else r2
    

'''
def solution(a, b):
    result_1 = int(str(a) + str(b))
    result_2 = int(str(b) + str(a))
    if result_1 >= result_2 : 
        answer = result_1
    else:
        answer = result_2
    return answer
'''