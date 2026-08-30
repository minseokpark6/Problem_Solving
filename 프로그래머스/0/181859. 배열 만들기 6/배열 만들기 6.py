def solution(arr):
    # 변수 정의 
    stk = []
    i = 0 
    
    # 새로운 배열 만들기 
    while i < len(arr):
        if stk:
            if stk[-1] == arr[i]:
                stk.pop()
            elif stk[-1] != arr[i]:
                stk.append(arr[i])
        else:
            stk.append(arr[i])
        
        i += 1
    
    # 출력
    return stk if stk else [-1]
                

    

'''
def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if len(answer) == 0:
            answer.append(arr[i])
            i += 1
        elif (len(answer) > 0) and (answer[-1] == arr[i]):
            answer.pop()
            i += 1
        elif (len(answer) > 0) and (answer[-1] != arr[i]):
            answer.append(arr[i])
            i += 1
    if len(answer) == 0:
        return [-1]
    else:
        return answer
'''