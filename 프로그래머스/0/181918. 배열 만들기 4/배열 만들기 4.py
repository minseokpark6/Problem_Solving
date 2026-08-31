def solution(arr):
    # 변수 정의
    stk = []
    i = 0
    
    # 새로운 배열 만들기
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
        
    # 출력
    return stk
    

'''
def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
            
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
            
        elif stk[-1] >= arr[i]:
            del stk[-1]
        
    return stk
'''