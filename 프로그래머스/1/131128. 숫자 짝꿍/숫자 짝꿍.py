from collections import Counter

def solution(X, Y):
    # X, Y에 들어가 있는 숫자 및 횟수 딕셔너리에 저장
    y = dict(Counter(Y))

    # 공통된 수 확인 
    result = []
    for i in X:
        if (i in y) and (y[i] > 0):
            y[i] -= 1
            result.append(i)

    # 가장 큰수로 반환 
    result.sort(reverse = True)
    
    # 출력
    # 공통 수가 없는 경우 / 0으로만 이루어져 있는 경우
    if not result:
        return "-1"
    elif all(x == "0" for x in result):
        return "0"

    # 그 외의 경우
    return "".join(result)




"""
# 실패 - 시간 초과 

##############
이 부분 때문 일것으로 추측

# 공통의 정수 확인 
for i in a:
    if i in b:
        result.append(i)
        b.remove(i)
###############



def solution(X, Y):
    a, b = list(X), list(Y)
    result = []
    
    # 공통의 정수 확인 
    for i in a:
        if i in b:
            result.append(i)
            b.remove(i)

    # 공통 수가 없는 경우
    if not result:
        result.append("-1")
    
    # 0으로만 이루어져 있는 경우 
    if all(x == "0" for x in result):
        result = ["0"]

    # 가장 큰수로 반환 
    result = sorted(result, reverse = True)

    # 출력
    return "".join(result)
"""
    